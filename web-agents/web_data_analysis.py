import pandas as pd
import numpy as np

INPUT_JSON_FILE = 'questions.json'
OUTPUT_HTML_FILE = 'output-questions.html'
OUTPUT_JSON_FILE = 'output-questions.json'
STYLES_HREF = '<head><link rel="stylesheet" type="text/css" href="table.css"></head>'

def wrap_anchors(df):
    return df['url'].apply(lambda u: '<a href="' + u + '">' + u[u.find('questions')+10:len(u)] + '</a>')

def add_styles():
  with open(OUTPUT_HTML_FILE, 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write(STYLES_HREF + '\n' + content)

pd.set_option('display.max_colwidth', -1)

df = pd.read_json(INPUT_JSON_FILE).drop("short_description", 1).drop("tag", 1)

df = df.sort_values(['answers', 'votes', 'views'], ascending=[True, False, False])
df['url'] = wrap_anchors(df)
df.to_json(OUTPUT_JSON_FILE)
df.to_html(OUTPUT_HTML_FILE, escape=False)
add_styles()
