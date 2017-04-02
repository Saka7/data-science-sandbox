import sys
import datetime
import random as r
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv, DataFrame
from scipy.optimize import curve_fit

def cubic(x, a, b, c, d):
  """
    @type x: number
    @type a: number
    @type b: number
    @type c: number
    @type d: number
    
    Calculates cubic function a*x^3+b*x^2+c*x+d
    @rtype: number
    @return: result of cubic function calculation
  """
  return a * (x ** 3) + b * (x ** 2) + c * x + d

def normalize(points, min):
  """
    @type points: array
    @param points: array to be normalized
    @type min: number
    @param min: min value of normalized array 
    Normalizes array
  """
  for i in range(len(points)):
    if points[i] < min:
      points[i] = min + 0.1

def load_data(csv_file):
  """
    @type  csv_file: string 
    @param csv_file: path to csv file
    Loads data from specified csv file
    @rtype: pandas.DataFrame
    @return: DataFrame from csv file without Month column 
  """
  return pd.read_csv(csv_file).drop('Month', 1)

def fill_with_NaNs(amount, data_frame):
  """
    @type amount: integer
    @param amount: numbers of rows to be filled with NaNs
    @type data_frame: pandas.DataFrame
    @param data_frame: dataFrame to be filled by NaNs
    Fills DataFrame with NaN's
  """
  for column in range(amount):
    data_frame.loc[len(data_frame)] = [None for i in range(len(data_frame.columns))]

def generate_date_rows(base_date, amount):
  """
    @type base_date: datetime
    @param base_date: initial date
    @type amount: integer
    @param amount: amount of rows(months) to be generated
    Generate dates(Year-Month) for all rows from specified initial date
    @rtype: numpy.Array
    @return: array of generate dates
  """ 
  return np.array([(base_date + datetime.timedelta(i*365/12)).strftime("%Y-%m") for i in range(amount)])
  
def extrapolate(data_frame):
  """
    @type data_frame: pandas.DataFrame
    @param data_frame: dataFrame to be extrapolated
  
    Extrapolates specified dataFrame (NaN values)
  """
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

if __name__ == "__main__":
  plt.style.use('ggplot')
  csv_file = "web-frameworks-trends.csv"
  # Loads data from CSV file
  df = load_data(csv_file)
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