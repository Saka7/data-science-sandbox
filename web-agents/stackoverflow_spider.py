import json
import time
import scrapy
import logging

OUTPUT_FILE = "questions.json"
DELAY = 5 # seconds

class StackOverflowQuestion:

  def __init__(self, tag="", title="", url="", short_description="", votes=0, answers=0, views=0):
    self.tag = tag
    self.title = title
    self.url = url
    self.short_description = short_description
    self.votes = votes
    self.answers = answers
    self.views = views

  def __str__(self):
    return json.dumps(self, default=lambda o: o.__dict__)

  def __repr__(self):
    return '\n\tTITLE: {}\n\tURL: {}\n\tVOTES: {}\n\tANSWERS: {}\n\tVIEWS: {}\n'.format(
      self.title, self.url, self.votes, self.answers, self.views
    )

class StackOverflowSpider(scrapy.Spider):
  name = 'stackoverflow-spider'

  def __init__(self, category='javascript', *args, **kwargs):
    super(StackOverflowSpider, self).__init__(*args, **kwargs)
    self.start_urls = ['https://stackoverflow.com/questions/tagged/' + str(category)]
    self.category = category

  def parse(self, response):
    questions = []
    for q in response.css('.question-summary'):
      question = StackOverflowQuestion(tag = self.category)
      question.title = q.css('div.summary > h3 > a ::text').extract_first()

      url = q.css('div.summary > h3 > a ::attr(href)').extract_first()
      if url:
        question.url = "https://stackoverflow.com" + url

      question.short_description = q.css('div.summary > div.excerpt ::text').extract_first()

      votes = q.css('div.statscontainer > div.stats > div.vote > div > span > strong ::text').extract_first()
      if votes:
        votes = int(votes)
      question.votes = votes

      answered = q.css('div.statscontainer > div.stats > div.status.answered > strong ::text').extract_first()
      unanswered = q.css('div.statscontainer > div.stats > div.status.unanswered > strong ::text').extract_first()
      if answered:
        question.answers = int(answered)
      elif unanswered:
        question.answers = int(unanswered)

      views = q.css('div.statscontainer > div.views ::attr(title)').extract_first()
      if views:
        views = int(views[0:views.find('view') - 1])
      question.views= views

      questions.append(question)

      yield {'QUESTION': question}

    with open(OUTPUT_FILE, "w") as questions_file:
      questions_file.write(json.dumps(questions, default=lambda o: o.__dict__))
    time.sleep(DELAY)
    next_page = response.css('#mainbar > div.pager.fl > a[rel=next] ::attr(href)').extract_first()
    if next_page:
      yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
    else:
      yield {'Your reach last page': next_page}

