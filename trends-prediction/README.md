
# Predicting trends using pandas

We are going to compare and predict popularity change of trending web technologies and frameworks (Ruby on Rails, Node.js, Python/Django, PHP/Laravel).

Let’s first get some data from Google Trends. To download CSV file just click on button on the top left corner of chart, then choose CSV from drop-down menu.

First of all we are going to visualize data stored in CSV(`web-frameworks-trends.csv`), which we just have downloaded from Google Trends.


```python
import sys
import datetime
import random as r
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv, DataFrame
from scipy.optimize import curve_fit

# Change charts style 
plt.style.use('ggplot')
# Load CSV data to DataFrame
df = pd.read_csv("web-frameworks-trends.csv")
# Set Index Column
df = df.set_index('Month')
# Plot line chart
df.plot.line()
plt.show()
```


![png](trends-prediction_files/trends-prediction_1_0.png)


To extrapolate the function we need to specify the end point of new function. One the way of doing this is filling out DataFrame by certain amount of rows(monthes) with NaN’s and generated dates.


```python
def fill_with_NaNs(amount, data_frame):
  for column in range(amount):
    data_frame.loc[len(data_frame)] = [None for i in range(len(data_frame.columns))]
    
def generate_date_rows(base_date, amount):
  return np.array([(base_date + datetime.timedelta(i*365/12)).strftime("%Y-%m") for i in range(amount)])

df = pd.read_csv("web-frameworks-trends.csv").drop('Month', 1)
# Months
months = 24 # Five years
# Fill specified amount of rows of dataframe with NaN's 
fill_with_NaNs(months, df)
# Generate dates(Year-Month) for all rows from specified initial date
date_rows = generate_date_rows(datetime.datetime(2004, 1, 1), len(df.index))
# Add date to dataframe
df['Month'] = pd.Series(date_rows, index=df.index)
# Set Date as index column
df = df.set_index('Month')
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Node.js</th>
      <th>Ruby on Rails</th>
      <th>Django</th>
      <th>Laravel</th>
    </tr>
    <tr>
      <th>Month</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2004-01</th>
      <td>13.0</td>
      <td>6.0</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2004-01</th>
      <td>14.0</td>
      <td>6.0</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2004-03</th>
      <td>13.0</td>
      <td>6.0</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2004-04</th>
      <td>13.0</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2004-05</th>
      <td>14.0</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2004-06</th>
      <td>15.0</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2004-07</th>
      <td>14.0</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2004-07</th>
      <td>15.0</td>
      <td>7.0</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2004-08</th>
      <td>14.0</td>
      <td>6.0</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2004-09</th>
      <td>13.0</td>
      <td>6.0</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2004-10</th>
      <td>13.0</td>
      <td>6.0</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2004-11</th>
      <td>14.0</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2004-12</th>
      <td>13.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2005-01</th>
      <td>15.0</td>
      <td>9.0</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2005-03</th>
      <td>14.0</td>
      <td>11.0</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2005-04</th>
      <td>13.0</td>
      <td>11.0</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2005-05</th>
      <td>13.0</td>
      <td>13.0</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2005-06</th>
      <td>13.0</td>
      <td>15.0</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2005-07</th>
      <td>12.0</td>
      <td>17.0</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2005-07</th>
      <td>12.0</td>
      <td>22.0</td>
      <td>5.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2005-08</th>
      <td>11.0</td>
      <td>21.0</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2005-09</th>
      <td>12.0</td>
      <td>27.0</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2005-10</th>
      <td>12.0</td>
      <td>28.0</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2005-11</th>
      <td>11.0</td>
      <td>32.0</td>
      <td>5.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2005-12</th>
      <td>11.0</td>
      <td>29.0</td>
      <td>5.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2006-01</th>
      <td>12.0</td>
      <td>34.0</td>
      <td>5.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2006-03</th>
      <td>12.0</td>
      <td>37.0</td>
      <td>5.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2006-04</th>
      <td>12.0</td>
      <td>39.0</td>
      <td>5.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2006-05</th>
      <td>12.0</td>
      <td>37.0</td>
      <td>6.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2006-06</th>
      <td>11.0</td>
      <td>36.0</td>
      <td>6.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2016-02</th>
      <td>39.0</td>
      <td>17.0</td>
      <td>15.0</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>2016-03</th>
      <td>39.0</td>
      <td>17.0</td>
      <td>15.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>2016-04</th>
      <td>39.0</td>
      <td>16.0</td>
      <td>14.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>2016-05</th>
      <td>38.0</td>
      <td>16.0</td>
      <td>14.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>2016-06</th>
      <td>38.0</td>
      <td>16.0</td>
      <td>14.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>2016-07</th>
      <td>39.0</td>
      <td>16.0</td>
      <td>14.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>2016-08</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2016-09</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2016-10</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2016-11</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2016-12</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-01</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-02</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-03</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-04</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-05</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-06</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-07</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-08</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-09</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-10</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-11</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-12</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2018-01</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2018-02</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2018-03</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2018-04</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2018-05</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2018-06</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2018-07</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>176 rows × 4 columns</p>
</div>




```python
df.plot.line()
plt.show()
```


![png](trends-prediction_files/trends-prediction_4_0.png)


## EXTRAPOLATING FUNCTION

> In mathematics, extrapolation is the process of estimating, beyond the original observation range, the value of a variable on the basis of its relationship with another variable.

One way to extrapolate function is by curve fitting some general parameterized equation to the data to find parameter values. The limiting issue with this approach is that some assumption about trend must be made when the parameterized equation is selected. This can be found through trial and error or it can be inferred from the source of the data.

For now we’ll keep it simple and extrapolate function with 3rd order polynomial.
`f(x) = a x3 + b x2 + c x + d`

Here is an example of DataFrame extrapolation.


```python
def cubic(x, a, b, c, d):
  return a * (x ** 3) + b * (x ** 2) + c * x + d

def extrapolate(data_frame):
  # Create copy of data to remove NaNs for curve fitting
  fit_df = data_frame.dropna()
  # Place to store function parameters for each column
  col_params = {}
  # Curve fit each column
  for col in fit_df.columns:
      # Get x & y
      x = fit_df.index.astype(float).values
      y = fit_df[col].values
      # Curve fit column and get curve parameters
      params = curve_fit(cubic, x, y)
      # Store optimized parameters
      col_params[col] = params[0]
  for col in data_frame.columns:
      # Get the index values for NaNs in the column
      x = data_frame[pd.isnull(data_frame[col])].index.astype(float).values
      # Extrapolate those points with the fitted function
      points = cubic(x, *col_params[col])
      data_frame[col][x] = points
```


```python
df = pd.read_csv("web-frameworks-trends.csv").drop('Month', 1)
# Months
months = 24 # Five years
# Fill specified amount of rows of dataframe with NaN's 
fill_with_NaNs(months, df)
# Extrapolates dataframe
extrapolate(df)
```


```python
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Node.js</th>
      <th>Ruby on Rails</th>
      <th>Django</th>
      <th>Laravel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>13.000000</td>
      <td>6.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14.000000</td>
      <td>6.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13.000000</td>
      <td>6.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13.000000</td>
      <td>5.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>14.000000</td>
      <td>5.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>15.000000</td>
      <td>5.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>14.000000</td>
      <td>5.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15.000000</td>
      <td>7.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>14.000000</td>
      <td>6.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>13.000000</td>
      <td>6.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>10</th>
      <td>13.000000</td>
      <td>6.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>11</th>
      <td>14.000000</td>
      <td>7.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13.000000</td>
      <td>8.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>15.000000</td>
      <td>9.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14.000000</td>
      <td>11.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>15</th>
      <td>13.000000</td>
      <td>11.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>16</th>
      <td>13.000000</td>
      <td>13.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>13.000000</td>
      <td>15.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>18</th>
      <td>12.000000</td>
      <td>17.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>19</th>
      <td>12.000000</td>
      <td>22.000000</td>
      <td>5.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>11.000000</td>
      <td>21.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>21</th>
      <td>12.000000</td>
      <td>27.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>22</th>
      <td>12.000000</td>
      <td>28.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>23</th>
      <td>11.000000</td>
      <td>32.000000</td>
      <td>5.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>24</th>
      <td>11.000000</td>
      <td>29.000000</td>
      <td>5.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25</th>
      <td>12.000000</td>
      <td>34.000000</td>
      <td>5.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>26</th>
      <td>12.000000</td>
      <td>37.000000</td>
      <td>5.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>27</th>
      <td>12.000000</td>
      <td>39.000000</td>
      <td>5.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>12.000000</td>
      <td>37.000000</td>
      <td>6.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>29</th>
      <td>11.000000</td>
      <td>36.000000</td>
      <td>6.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>146</th>
      <td>39.000000</td>
      <td>17.000000</td>
      <td>15.000000</td>
      <td>11.000000</td>
    </tr>
    <tr>
      <th>147</th>
      <td>39.000000</td>
      <td>17.000000</td>
      <td>15.000000</td>
      <td>12.000000</td>
    </tr>
    <tr>
      <th>148</th>
      <td>39.000000</td>
      <td>16.000000</td>
      <td>14.000000</td>
      <td>12.000000</td>
    </tr>
    <tr>
      <th>149</th>
      <td>38.000000</td>
      <td>16.000000</td>
      <td>14.000000</td>
      <td>12.000000</td>
    </tr>
    <tr>
      <th>150</th>
      <td>38.000000</td>
      <td>16.000000</td>
      <td>14.000000</td>
      <td>12.000000</td>
    </tr>
    <tr>
      <th>151</th>
      <td>39.000000</td>
      <td>16.000000</td>
      <td>14.000000</td>
      <td>14.000000</td>
    </tr>
    <tr>
      <th>152</th>
      <td>40.810921</td>
      <td>24.251140</td>
      <td>12.807951</td>
      <td>14.337858</td>
    </tr>
    <tr>
      <th>153</th>
      <td>41.478122</td>
      <td>25.009518</td>
      <td>12.472362</td>
      <td>14.786680</td>
    </tr>
    <tr>
      <th>154</th>
      <td>42.153539</td>
      <td>25.803842</td>
      <td>12.125475</td>
      <td>15.244268</td>
    </tr>
    <tr>
      <th>155</th>
      <td>42.837205</td>
      <td>26.634661</td>
      <td>11.767171</td>
      <td>15.710705</td>
    </tr>
    <tr>
      <th>156</th>
      <td>43.529153</td>
      <td>27.502522</td>
      <td>11.397330</td>
      <td>16.186070</td>
    </tr>
    <tr>
      <th>157</th>
      <td>44.229416</td>
      <td>28.407976</td>
      <td>11.015834</td>
      <td>16.670445</td>
    </tr>
    <tr>
      <th>158</th>
      <td>44.938028</td>
      <td>29.351570</td>
      <td>10.622563</td>
      <td>17.163912</td>
    </tr>
    <tr>
      <th>159</th>
      <td>45.655021</td>
      <td>30.333853</td>
      <td>10.217397</td>
      <td>17.666551</td>
    </tr>
    <tr>
      <th>160</th>
      <td>46.380428</td>
      <td>31.355375</td>
      <td>9.800217</td>
      <td>18.178443</td>
    </tr>
    <tr>
      <th>161</th>
      <td>47.114283</td>
      <td>32.416684</td>
      <td>9.370904</td>
      <td>18.699671</td>
    </tr>
    <tr>
      <th>162</th>
      <td>47.856618</td>
      <td>33.518328</td>
      <td>8.929339</td>
      <td>19.230314</td>
    </tr>
    <tr>
      <th>163</th>
      <td>48.607467</td>
      <td>34.660857</td>
      <td>8.475402</td>
      <td>19.770454</td>
    </tr>
    <tr>
      <th>164</th>
      <td>49.366862</td>
      <td>35.844819</td>
      <td>8.008973</td>
      <td>20.320173</td>
    </tr>
    <tr>
      <th>165</th>
      <td>50.134837</td>
      <td>37.070763</td>
      <td>7.529934</td>
      <td>20.879551</td>
    </tr>
    <tr>
      <th>166</th>
      <td>50.911424</td>
      <td>38.339238</td>
      <td>7.038165</td>
      <td>21.448670</td>
    </tr>
    <tr>
      <th>167</th>
      <td>51.696658</td>
      <td>39.650792</td>
      <td>6.533547</td>
      <td>22.027610</td>
    </tr>
    <tr>
      <th>168</th>
      <td>52.490569</td>
      <td>41.005975</td>
      <td>6.015959</td>
      <td>22.616453</td>
    </tr>
    <tr>
      <th>169</th>
      <td>53.293193</td>
      <td>42.405334</td>
      <td>5.485284</td>
      <td>23.215281</td>
    </tr>
    <tr>
      <th>170</th>
      <td>54.104561</td>
      <td>43.849420</td>
      <td>4.941402</td>
      <td>23.824173</td>
    </tr>
    <tr>
      <th>171</th>
      <td>54.924707</td>
      <td>45.338780</td>
      <td>4.384193</td>
      <td>24.443212</td>
    </tr>
    <tr>
      <th>172</th>
      <td>55.753665</td>
      <td>46.873963</td>
      <td>3.813538</td>
      <td>25.072479</td>
    </tr>
    <tr>
      <th>173</th>
      <td>56.591466</td>
      <td>48.455518</td>
      <td>3.229317</td>
      <td>25.712054</td>
    </tr>
    <tr>
      <th>174</th>
      <td>57.438144</td>
      <td>50.083994</td>
      <td>2.631412</td>
      <td>26.362019</td>
    </tr>
    <tr>
      <th>175</th>
      <td>58.293732</td>
      <td>51.759940</td>
      <td>2.019703</td>
      <td>27.022455</td>
    </tr>
  </tbody>
</table>
<p>176 rows × 4 columns</p>
</div>




```python
df.plot.line()
plt.show()
```


![png](trends-prediction_files/trends-prediction_9_0.png)


## ADDING RANDOM CHANGES

Typically, the quality of a particular method of extrapolation is limited by the assumptions about the function made by the method. If the method assumes the data are smooth, then a non-smooth function will be poorly extrapolated.

In the future we need to replace current polynomial extrapolation function with better one(some analytic extrapolation). But for now let’s just make our chat looks more “realistic” by adding some random changes to lines.


```python
def load_data(csv_file):
  return pd.read_csv(csv_file).drop('Month', 1)

def normalize(points, min):
  for i in range(len(points)):
    if points[i] < min:
      points[i] = min + 0.1

def extrapolate(data_frame):
  # Create copy of data to remove NaNs for curve fitting
  fit_df = data_frame.dropna()
  # Place to store function parameters for each column
  col_params = {}
  # Curve fit each column
  for col in fit_df.columns:
      # Get x & y
      x = fit_df.index.astype(float).values
      y = fit_df[col].values
      # Curve fit column and get curve parameters
      params = curve_fit(cubic, x, y)
      # Store optimized parameters
      col_params[col] = params[0]
  for col in data_frame.columns:
      # Get the index values for NaNs in the column
      x = data_frame[pd.isnull(data_frame[col])] \
        .index.astype(float).values
      # Extrapolate those points with the fitted function
      points = cubic(x, *col_params[col])
      normalize(points, 0)
      # Add random changes
      for i in range(len(points)):
        if int(points[i]) % int(r.random() * 3 + 1) is 0:
          points[i] += r.random() * 4 - 2
      normalize(points, 0)
      data_frame[col][x] = points
```


```python
df = load_data("web-frameworks-trends.csv")
# Months
months = 24 # Five years
# Fill specified amount of rows of dataframe with NaN's 
fill_with_NaNs(months, df)
# Interpolate
df.interpolate()
# Extrapolate dataframe
extrapolate(df)
# Generate dates(Year-Month) for all rows from specified initial date
date_rows = generate_date_rows(datetime.datetime(2004, 1, 1), len(df.index))
# Add date to dataframe
df['Month'] = pd.Series(date_rows, index=df.index)
# Set Date as index column
df = df.set_index('Month')
# Plot line chart
df.plot.line()
plt.show()
```


![png](trends-prediction_files/trends-prediction_12_0.png)



```python
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Node.js</th>
      <th>Ruby on Rails</th>
      <th>Django</th>
      <th>Laravel</th>
    </tr>
    <tr>
      <th>Month</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2004-01</th>
      <td>13.000000</td>
      <td>6.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2004-01</th>
      <td>14.000000</td>
      <td>6.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2004-03</th>
      <td>13.000000</td>
      <td>6.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2004-04</th>
      <td>13.000000</td>
      <td>5.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2004-05</th>
      <td>14.000000</td>
      <td>5.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2004-06</th>
      <td>15.000000</td>
      <td>5.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2004-07</th>
      <td>14.000000</td>
      <td>5.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2004-07</th>
      <td>15.000000</td>
      <td>7.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2004-08</th>
      <td>14.000000</td>
      <td>6.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2004-09</th>
      <td>13.000000</td>
      <td>6.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2004-10</th>
      <td>13.000000</td>
      <td>6.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2004-11</th>
      <td>14.000000</td>
      <td>7.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2004-12</th>
      <td>13.000000</td>
      <td>8.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2005-01</th>
      <td>15.000000</td>
      <td>9.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2005-03</th>
      <td>14.000000</td>
      <td>11.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2005-04</th>
      <td>13.000000</td>
      <td>11.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2005-05</th>
      <td>13.000000</td>
      <td>13.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2005-06</th>
      <td>13.000000</td>
      <td>15.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2005-07</th>
      <td>12.000000</td>
      <td>17.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2005-07</th>
      <td>12.000000</td>
      <td>22.000000</td>
      <td>5.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2005-08</th>
      <td>11.000000</td>
      <td>21.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2005-09</th>
      <td>12.000000</td>
      <td>27.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2005-10</th>
      <td>12.000000</td>
      <td>28.000000</td>
      <td>4.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2005-11</th>
      <td>11.000000</td>
      <td>32.000000</td>
      <td>5.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2005-12</th>
      <td>11.000000</td>
      <td>29.000000</td>
      <td>5.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2006-01</th>
      <td>12.000000</td>
      <td>34.000000</td>
      <td>5.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2006-03</th>
      <td>12.000000</td>
      <td>37.000000</td>
      <td>5.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2006-04</th>
      <td>12.000000</td>
      <td>39.000000</td>
      <td>5.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2006-05</th>
      <td>12.000000</td>
      <td>37.000000</td>
      <td>6.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2006-06</th>
      <td>11.000000</td>
      <td>36.000000</td>
      <td>6.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2016-02</th>
      <td>39.000000</td>
      <td>17.000000</td>
      <td>15.000000</td>
      <td>11.000000</td>
    </tr>
    <tr>
      <th>2016-03</th>
      <td>39.000000</td>
      <td>17.000000</td>
      <td>15.000000</td>
      <td>12.000000</td>
    </tr>
    <tr>
      <th>2016-04</th>
      <td>39.000000</td>
      <td>16.000000</td>
      <td>14.000000</td>
      <td>12.000000</td>
    </tr>
    <tr>
      <th>2016-05</th>
      <td>38.000000</td>
      <td>16.000000</td>
      <td>14.000000</td>
      <td>12.000000</td>
    </tr>
    <tr>
      <th>2016-06</th>
      <td>38.000000</td>
      <td>16.000000</td>
      <td>14.000000</td>
      <td>12.000000</td>
    </tr>
    <tr>
      <th>2016-07</th>
      <td>39.000000</td>
      <td>16.000000</td>
      <td>14.000000</td>
      <td>14.000000</td>
    </tr>
    <tr>
      <th>2016-08</th>
      <td>40.810921</td>
      <td>24.971908</td>
      <td>14.419288</td>
      <td>13.949269</td>
    </tr>
    <tr>
      <th>2016-09</th>
      <td>41.478122</td>
      <td>25.009518</td>
      <td>13.237933</td>
      <td>14.786680</td>
    </tr>
    <tr>
      <th>2016-10</th>
      <td>43.561529</td>
      <td>24.944315</td>
      <td>12.305218</td>
      <td>13.550968</td>
    </tr>
    <tr>
      <th>2016-11</th>
      <td>42.003058</td>
      <td>26.634661</td>
      <td>11.767171</td>
      <td>16.208225</td>
    </tr>
    <tr>
      <th>2016-12</th>
      <td>43.472450</td>
      <td>26.041132</td>
      <td>11.191040</td>
      <td>16.858414</td>
    </tr>
    <tr>
      <th>2017-01</th>
      <td>44.229416</td>
      <td>27.240278</td>
      <td>11.015834</td>
      <td>16.670445</td>
    </tr>
    <tr>
      <th>2017-02</th>
      <td>44.217257</td>
      <td>29.351570</td>
      <td>10.622563</td>
      <td>17.163912</td>
    </tr>
    <tr>
      <th>2017-03</th>
      <td>45.655021</td>
      <td>30.470682</td>
      <td>10.217397</td>
      <td>17.666551</td>
    </tr>
    <tr>
      <th>2017-04</th>
      <td>47.698055</td>
      <td>31.355375</td>
      <td>10.874544</td>
      <td>18.327241</td>
    </tr>
    <tr>
      <th>2017-05</th>
      <td>47.114283</td>
      <td>32.999912</td>
      <td>10.682863</td>
      <td>17.539503</td>
    </tr>
    <tr>
      <th>2017-06</th>
      <td>47.856618</td>
      <td>33.518328</td>
      <td>8.929339</td>
      <td>19.753994</td>
    </tr>
    <tr>
      <th>2017-07</th>
      <td>47.524461</td>
      <td>34.660857</td>
      <td>8.475402</td>
      <td>19.770454</td>
    </tr>
    <tr>
      <th>2017-08</th>
      <td>48.454385</td>
      <td>35.844819</td>
      <td>8.008973</td>
      <td>19.265301</td>
    </tr>
    <tr>
      <th>2017-09</th>
      <td>50.134837</td>
      <td>37.070763</td>
      <td>7.529934</td>
      <td>20.030932</td>
    </tr>
    <tr>
      <th>2017-10</th>
      <td>48.989920</td>
      <td>39.169027</td>
      <td>7.038165</td>
      <td>23.056307</td>
    </tr>
    <tr>
      <th>2017-11</th>
      <td>51.696658</td>
      <td>41.507645</td>
      <td>6.023999</td>
      <td>22.027610</td>
    </tr>
    <tr>
      <th>2017-12</th>
      <td>51.082643</td>
      <td>41.005975</td>
      <td>7.551405</td>
      <td>22.827126</td>
    </tr>
    <tr>
      <th>2018-01</th>
      <td>53.293193</td>
      <td>42.960312</td>
      <td>6.328849</td>
      <td>23.215281</td>
    </tr>
    <tr>
      <th>2018-02</th>
      <td>53.846993</td>
      <td>43.849420</td>
      <td>4.941402</td>
      <td>23.824173</td>
    </tr>
    <tr>
      <th>2018-03</th>
      <td>55.571019</td>
      <td>45.246200</td>
      <td>4.384193</td>
      <td>23.295001</td>
    </tr>
    <tr>
      <th>2018-04</th>
      <td>54.794054</td>
      <td>45.337545</td>
      <td>5.680177</td>
      <td>25.072479</td>
    </tr>
    <tr>
      <th>2018-05</th>
      <td>57.450015</td>
      <td>50.278382</td>
      <td>3.229317</td>
      <td>25.712054</td>
    </tr>
    <tr>
      <th>2018-06</th>
      <td>57.608931</td>
      <td>49.960222</td>
      <td>0.966132</td>
      <td>26.028253</td>
    </tr>
    <tr>
      <th>2018-07</th>
      <td>56.354749</td>
      <td>53.141965</td>
      <td>3.739218</td>
      <td>26.141025</td>
    </tr>
  </tbody>
</table>
<p>176 rows × 4 columns</p>
</div>




```python

```
