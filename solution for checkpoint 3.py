#!/usr/bin/env python
# coding: utf-8

# # Checkpoint Three: Cleaning Data
# 
# Now you are ready to clean your data. Before starting coding, provide the link to your dataset below.
# 
# My dataset: https://github.com/Faiqa-Sajid/Pandas-Data-Science-Tasks/tree/master/SalesAnalysis/Output
# 
# Import the necessary libraries and create your dataframe(s).

# In[9]:


import pandas as pd
import matplotlib.pyplot as plt
all_data = pd.read_csv(r"C:\Anaconda\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data/all_data.csv")


# ## Missing Data
# 
# Test your dataset for missing data and handle it as needed. Make notes in the form of code comments as to your thought process.

# Code to view all the NaN values of my dataset :

# In[4]:


nan_df = all_data[all_data.isna().any(axis=1)]
nan_df.head()


# Now that I know exactly where my NaN values are ; I will drop all of those in order to successfully add a month column to my previous notebook:

# In[5]:


all_data = all_data.dropna(how='all')
all_data.head()


# In[ ]:





# In[ ]:





# ## Irregular Data
# 
# Detect outliers in your dataset and handle them as needed. Use code comments to make notes about your thought process.

# In[ ]:





# ## Unnecessary Data
# 
# Look for the different types of unnecessary data in your dataset and address it as needed. Make sure to use code comments to illustrate your thought process.

# In my previous notebook while I was converting the months column format to strings I encountered this error: invalid literal for int() with base 10: 'Or' So now the task is to Find 'Or' and delete it :

# In[6]:


temp_df =  all_data[all_data['Order Date'].str[0:2] == 'Or']
temp_df.head()


# In[7]:


#deleting 'Or' values :
all_data =  all_data[all_data['Order Date'].str[0:2] != 'Or']


# ## Inconsistent Data
# 
# Check for inconsistent data and address any that arises. As always, use code comments to illustrate your thought process.

# In[ ]:





# In[ ]:





# # Exporting cleaned data as a CSV file :

# In[22]:


#I need to research and fix this issue. 
all_data.to_csv(r"C:\Anaconda\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data/all_dataexport.csv", sep=",")


# ## Summarize Your Results
# 
# Make note of your answers to the following questions.
# 
# 1. Did you find all four types of dirty data in your dataset?
# My dataset had only used two of data cleaning mehtods:Missing data and Unnecessary data.
# 2. Did the process of cleaning your data give you new insights into your dataset?
# Yes ! It helped me to analyze the data deeper in order to know what items sold the most in what months . And also what cities were higher in sales in compared to others. Cleaning also allowed me to add specific columns that I needed for my analysis.
# 3. Is there anything you would like to make note of when it comes to manipulating the data and making visualizations?
# I thnik it will be fun to show visualiztion of my sales analysis .
