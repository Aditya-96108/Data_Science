#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Data Frames I

#data fram is a two dimensional table consisting of rows and tables


# In[3]:


import pandas as pd


# In[5]:


df=pd.read_csv("C:/Users/91749/Downloads/german_credit_risk.csv")


# In[35]:


s=pd.Series([1,2,3,4,5])


# In[15]:


df.shape
s.shape
df.describe()
s.describe()


# In[17]:


df.index


# In[18]:


s.index


# In[23]:


df.head().value_counts


# In[25]:


df.dtypes


# In[26]:


s.dtypes


# In[28]:


df.values
#pandas store nan as floating numbers


# In[36]:


s.hasnans # return boolean if null values exists


# In[31]:


df.hasnans


# In[39]:


df.columns


# In[40]:


df.axes


# In[42]:


s.info()
df.info()


# In[43]:


#why saving accounts column has 817 rows , is it because remaining have null values stored : Yes
df.isnull().sum()


# In[60]:


dura= pd.read_csv("C:/Users/91749/Downloads/german_credit_risk.csv",usecols=["Duration"])
dura.sum(axis="index")


# In[63]:


duratio= pd.read_csv("C:/Users/91749/Downloads/german_credit_risk.csv",index_col=["Duration"])
duratio.head(7)


# In[73]:


duratio["Age"].sum(axis="columns")


# In[ ]:




