# -*- coding: utf-8 -*-
"""my_custom_utils.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S7CHFw7cRnlcd8-W6vEvp7BHWZSadf-z
"""
# This file is for data preparation and feature selection. It conatins the functions for both classification and regression problems but only usable for CSE-464 lab project.
# Commented out IPython magic to ensure Python compatibility.

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import mutual_info_classif, mutual_info_regression, SelectPercentile
from matplotlib import pyplot as plt
# %matplotlib inline

df=pd.read_csv('Copy of Depression and Happiness Factor Analysis.csv')

def data_preparation(data):
  """This funtion is for data preparation which returns the clean data. In order to do this, it drops the unnecessay columns and sets the index. 
  Then it encodes the categorical non-numeric data into numeric data using label encoder.

  Input:
      data: The dataframe.
  
  Output:
      Concatenation of encoded and numeric data.
  """
  data=data.drop(['Timestamp','Unnamed: 20'],axis=1)
  data=data.set_index('Which year are you in?')
  data_numeric=data.drop(data.iloc[:, [0,2,4,5,6,8,9,10,11,12,13,14,15,16]],axis=1)
  data_non_numeric=data.drop(data.iloc[:, [1,3,7,17]],axis=1)
  le=LabelEncoder()
  encode=data_non_numeric.apply(le.fit_transform)

  return pd.concat([encode,data_numeric],axis=1)


def important_features_visualization_classifier(data):
  """This function plots the importance features using mutual information classifier.

  Input:
      data: The dataframe.
  
  Output:
      Plots a horizontal bar chart of the important features in a descending order.
  """
  X=data.drop('How are you feeling right now?',axis=1)
  y=data['How are you feeling right now?']
  imp=mutual_info_classif(X,y)
  feat_imp=pd.Series(imp,data.columns[0:len(data.columns)-1])
  feat_imp.sort_values(ascending=False).plot(kind='barh',color='teal',figsize=(20,10))
  plt.show()


def important_features_visualization_regression(data):
  """This function plots the importance features using mutual information regression.

  Input:
      data: The dataframe.
  
  Output:
      Plots a horizontal bar chart of the important features in a descending order.
  """
  X=data.drop('How are you feeling right now?',axis=1)
  y=data['How are you feeling right now?']
  imp=mutual_info_regression(X,y)
  feat_imp=pd.Series(imp,data.columns[0:len(data.columns)-1])
  feat_imp.sort_values(ascending=False).plot(kind='barh',color='teal',figsize=(20,10))
  plt.show()


def feature_selection_classifier(data):
  """This function finds the important features using mutual information classifier under a percentile value.

  Input:
      data: The dataframe.
  
  Output:
      Returns the top important features under 30 percentiles.
  """
  X=data.drop('How are you feeling right now?',axis=1)
  y=data['How are you feeling right now?']
  select=SelectPercentile(mutual_info_classif,percentile=30)
  select.fit(X,y)

  return X.columns[select.get_support()]


def feature_selection_regression(data):
  """This function finds the important features using mutual information regression under a percentile value.

  Input:
      data: The dataframe.
  
  Output:
      Returns the top important features under 30 percentiles.
  """
  X=data.drop('How are you feeling right now?',axis=1)
  y=data['How are you feeling right now?']
  select=SelectPercentile(mutual_info_regression,percentile=30)
  select.fit(X,y)

  return X.columns[select.get_support()]


# For Linear Regression

def important_features_visualization_linear(data):
  """This function plots the importance features using mutual information regression. It is only for Linear_Regression.ipynb.

  Input:
      data: The dataframe.
  
  Output:
      Plots a horizontal bar chart of the important features in a descending order.
  """
  X=data.drop('On a scale of 1-100, how would you express this feeling?',axis=1)
  y=data['On a scale of 1-100, how would you express this feeling?']
  imp=mutual_info_regression(X,y)
  feat_imp=pd.Series(imp,data.columns[0:len(data.columns)-1])
  feat_imp.sort_values(ascending=False).plot(kind='barh',color='teal',figsize=(20,10))
  plt.show()

def feature_selection_linear(data):
  """This function finds the important features using mutual information regression under a percentile value. It is only for Linear_Regression.ipynb.

  Input:
      data: The dataframe.
  
  Output:
      Returns the top important features under 30 percentiles.
  """
  X=data.drop('On a scale of 1-100, how would you express this feeling?',axis=1)
  y=data['On a scale of 1-100, how would you express this feeling?']
  select=SelectPercentile(mutual_info_regression,percentile=30)
  select.fit(X,y)

  return X.columns[select.get_support()]
