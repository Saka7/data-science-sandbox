

```python
import pandas as pd
import numpy as np

INPUT_JSON_FILE = 'questions.json'

pd.set_option('display.max_colwidth', -1)
df = pd.read_json(INPUT_JSON_FILE).drop("short_description", 1).drop("tag", 1)
df = df.sort_values(['answers', 'votes', 'views'], ascending=[True, False, False])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>answers</th>
      <th>title</th>
      <th>url</th>
      <th>views</th>
      <th>votes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>0</td>
      <td>scipy.signal.resample: malfunction with even number of points?</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43283845/scipy-signal-resample-malfunction-with-even-number-of-points</td>
      <td>14</td>
      <td>1</td>
    </tr>
    <tr>
      <th>49</th>
      <td>0</td>
      <td>How do I plot a histogram of months with dates in matplotlib</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43283586/how-do-i-plot-a-histogram-of-months-with-dates-in-matplotlib</td>
      <td>9</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0</td>
      <td>Python array counter</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284525/python-array-counter</td>
      <td>46</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0</td>
      <td>'float' object has no attribute '__getitem__' in for loop</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284633/float-object-has-no-attribute-getitem-in-for-loop</td>
      <td>33</td>
      <td>0</td>
    </tr>
    <tr>
      <th>43</th>
      <td>0</td>
      <td>Incorrectly returning the value of a Node at position 'm' in a linked list</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43283705/incorrectly-returning-the-value-of-a-node-at-position-m-in-a-linked-list</td>
      <td>26</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>Python- Labeling items in a list by year</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284734/python-labeling-items-in-a-list-by-year</td>
      <td>23</td>
      <td>0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>0</td>
      <td>Python scriptline to get date&amp;time</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284121/python-scriptline-to-get-datetime</td>
      <td>18</td>
      <td>0</td>
    </tr>
    <tr>
      <th>36</th>
      <td>0</td>
      <td>define 2 GET ABSOLUTE URL method</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43283871/define-2-get-absolute-url-method</td>
      <td>16</td>
      <td>0</td>
    </tr>
    <tr>
      <th>32</th>
      <td>0</td>
      <td>Spectrogram of a wave file</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284049/spectrogram-of-a-wave-file</td>
      <td>15</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0</td>
      <td>Tkinter threading and return to text widget</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284439/tkinter-threading-and-return-to-text-widget</td>
      <td>13</td>
      <td>0</td>
    </tr>
    <tr>
      <th>41</th>
      <td>0</td>
      <td>Python Bokeh - Assign taptool to a subset of Glyphs</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43283717/python-bokeh-assign-taptool-to-a-subset-of-glyphs</td>
      <td>13</td>
      <td>0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>0</td>
      <td>plot_time and annoying “.f” in x-axis</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284370/plot-time-and-annoying-f-in-x-axis</td>
      <td>12</td>
      <td>0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>0</td>
      <td>Django - Redirecting after ajax post call with the data</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284153/django-redirecting-after-ajax-post-call-with-the-data</td>
      <td>12</td>
      <td>0</td>
    </tr>
    <tr>
      <th>35</th>
      <td>0</td>
      <td>Run all the code in a Django ModelForm __init__() method after an invalid form submission</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43283893/run-all-the-code-in-a-django-modelform-init-method-after-an-invalid-form-s</td>
      <td>12</td>
      <td>0</td>
    </tr>
    <tr>
      <th>38</th>
      <td>0</td>
      <td>Using python's pysftp, how do you generate a host key?</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43283855/using-pythons-pysftp-how-do-you-generate-a-host-key</td>
      <td>12</td>
      <td>0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0</td>
      <td>How can I avoid tox from reinstalling dependencies and deleting my break point?</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284343/how-can-i-avoid-tox-from-reinstalling-dependencies-and-deleting-my-break-point</td>
      <td>11</td>
      <td>0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>0</td>
      <td>Get function name as script parameter [duplicate]</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284300/get-function-name-as-script-parameter</td>
      <td>10</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>Require help understanding Flask url_for()</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284770/require-help-understanding-flask-url-for</td>
      <td>9</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0</td>
      <td>Python, evdev, usb barcode reader: how to decode the input data</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284404/python-evdev-usb-barcode-reader-how-to-decode-the-input-data</td>
      <td>9</td>
      <td>0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>0</td>
      <td>Carmen-Python: the JSON object must be str, not 'bytes'</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284298/carmen-python-the-json-object-must-be-str-not-bytes</td>
      <td>9</td>
      <td>0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>0</td>
      <td>PyCharm - Expected type 'Optional[IO[str]]', got 'TextIOWrapper[str]' instead</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284253/pycharm-expected-type-optionaliostr-got-textiowrapperstr-instead</td>
      <td>9</td>
      <td>0</td>
    </tr>
    <tr>
      <th>44</th>
      <td>0</td>
      <td>Stabilizing an Already Seeded Tensorflow Network and Predicting Confidence</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43283663/stabilizing-an-already-seeded-tensorflow-network-and-predicting-confidence</td>
      <td>8</td>
      <td>0</td>
    </tr>
    <tr>
      <th>40</th>
      <td>0</td>
      <td>Trouble importing from rpy2.robjects</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43283802/trouble-importing-from-rpy2-robjects</td>
      <td>7</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
      <td>Reshape batch of tensors into batch of vectors in TensorFlow</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284684/reshape-batch-of-tensors-into-batch-of-vectors-in-tensorflow</td>
      <td>6</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0</td>
      <td>Error loading MySQLdb module:_mysql.so: undefined symbol: mysql_shutdown</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284615/error-loading-mysqldb-module-mysql-so-undefined-symbol-mysql-shutdown</td>
      <td>6</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0</td>
      <td>cartToPolar in openCV gives only degrees between 0 and 90</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284603/carttopolar-in-opencv-gives-only-degrees-between-0-and-90</td>
      <td>5</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>How to use a Python weakref cache mapping keys to values, when values hold a reference to the keys?</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284711/how-to-use-a-python-weakref-cache-mapping-keys-to-values-when-values-hold-a-ref</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>47</th>
      <td>0</td>
      <td>add python as a CGI on a apache/php5-fpm enabled debian server</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43283627/add-python-as-a-cgi-on-a-apache-php5-fpm-enabled-debian-server</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0</td>
      <td>Why this script won't work if the while is set to true?</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284486/why-this-script-wont-work-if-the-while-is-set-to-true</td>
      <td>28</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>45</th>
      <td>0</td>
      <td>How to create an object from a class— getting an Attribute error</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43283657/how-to-create-an-object-from-a-class-getting-an-attribute-error</td>
      <td>22</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>30</th>
      <td>0</td>
      <td>sklearn - knn sklearn.neighbors kneighbors function producing unexpected result for text analysis?</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284115/sklearn-knn-sklearn-neighbors-kneighbors-function-producing-unexpected-result</td>
      <td>16</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0</td>
      <td>Check if geo coordinate point is land or ocean</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284606/check-if-geo-coordinate-point-is-land-or-ocean</td>
      <td>12</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Summing multiple dictionary values from a generator expression</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284804/summing-multiple-dictionary-values-from-a-generator-expression</td>
      <td>19</td>
      <td>-2</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0</td>
      <td>Why does python put a namespace here? [on hold]</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284383/why-does-python-put-a-namespace-here</td>
      <td>17</td>
      <td>-2</td>
    </tr>
    <tr>
      <th>24</th>
      <td>0</td>
      <td>How to debug “TypeError: 'NoneType' object has no attribute '__getitem__'”?</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284280/how-to-debug-typeerror-nonetype-object-has-no-attribute-getitem</td>
      <td>25</td>
      <td>-3</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0</td>
      <td>Python Sync Task [on hold]</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284529/python-sync-task</td>
      <td>24</td>
      <td>-7</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1</td>
      <td>Beautiful Soup: Data Values Not Matching Headings</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284399/beautiful-soup-data-values-not-matching-headings</td>
      <td>16</td>
      <td>1</td>
    </tr>
    <tr>
      <th>26</th>
      <td>1</td>
      <td>Interpolating climate data with irregular measurement intervals in Python with pandas and traces</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284165/interpolating-climate-data-with-irregular-measurement-intervals-in-python-with-p</td>
      <td>28</td>
      <td>0</td>
    </tr>
    <tr>
      <th>37</th>
      <td>1</td>
      <td>Dynamically adding elements to a NumPy array of unknown final length</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43283866/dynamically-adding-elements-to-a-numpy-array-of-unknown-final-length</td>
      <td>26</td>
      <td>0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>1</td>
      <td>Issues installing pynini</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284123/issues-installing-pynini</td>
      <td>15</td>
      <td>0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1</td>
      <td>Spark structured streaming with python</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284380/spark-structured-streaming-with-python</td>
      <td>14</td>
      <td>0</td>
    </tr>
    <tr>
      <th>34</th>
      <td>1</td>
      <td>What does this mean: “unable to send message, socket is not open”?</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43283951/what-does-this-mean-unable-to-send-message-socket-is-not-open</td>
      <td>13</td>
      <td>0</td>
    </tr>
    <tr>
      <th>46</th>
      <td>1</td>
      <td>Change range withouth scaling in matplot</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43283643/change-range-withouth-scaling-in-matplot</td>
      <td>13</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Spyder changes working directory (wdir) when running a script</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284787/spyder-changes-working-directory-wdir-when-running-a-script</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>48</th>
      <td>1</td>
      <td>Python ViolinPlots</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43283599/python-violinplots</td>
      <td>17</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2</td>
      <td>How to compute volatility (standard deviation) in rolling window in Pandas</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284304/how-to-compute-volatility-standard-deviation-in-rolling-window-in-pandas</td>
      <td>39</td>
      <td>1</td>
    </tr>
    <tr>
      <th>33</th>
      <td>2</td>
      <td>Python loop - help me understand</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43283960/python-loop-help-me-understand</td>
      <td>26</td>
      <td>0</td>
    </tr>
    <tr>
      <th>42</th>
      <td>2</td>
      <td>run python script from cmd with inputs</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43283714/run-python-script-from-cmd-with-inputs</td>
      <td>23</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>Which sparse Matrix representation to use with sklearn.svm.LinearSVC</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284717/which-sparse-matrix-representation-to-use-with-sklearn-svm-linearsvc</td>
      <td>6</td>
      <td>0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>5</td>
      <td>How to take all the words in a list element as a variable</td>
      <td>https://stackoverflow.com/questions/tagged/python/questions/43284071/how-to-take-all-the-words-in-a-list-element-as-a-variable</td>
      <td>47</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
