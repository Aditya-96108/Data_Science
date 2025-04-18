#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


csv_data= pd.read_csv("C:/Users/91749/Desktop/credit_risk_data.csv")


# In[5]:


csv_data.head(10)


# In[6]:


csv_data= pd.read_csv("C:/Users/91749/Desktop/credit_risk_data.csv",usecols=["Credit_Score"]).squeeze("columns")
csv_data


# In[7]:


csv_data.iloc[[0]]=100 #this will override the value which already exists there


# In[8]:


csv_data #updated value in this field 


# In[9]:


csv_data.loc[3]
csv_data.iloc[0]=222
csv_data[0]=111
csv_data


# In[10]:


#Learning Copy Method
#understanding the problem
csv_data= pd.read_csv("C:/Users/91749/Desktop/credit_risk_data.csv",usecols=["Loan_Amount"])
csv_squeeze=csv_data.squeeze("columns")
csv_squeeze


# In[11]:


csv_squeeze[0]=0


# In[12]:


csv_squeeze


# In[13]:


csv_data #changes applied tto the copy of original gets reflected on both sides 


# In[14]:


#we can use .copy() after squeeze to avoid the changes


# In[15]:


csv_data= pd.read_csv("C:/Users/91749/Desktop/credit_risk_data.csv",usecols=["Loan_Amount"]).squeeze("columns")


# In[16]:


csv_data.count() #excludes null values
csv_data.size  #includes all the null values


# In[17]:


csv_data.count()
csv_data.sum()
csv_data.product() #Not Understood
csv_data.mean()
csv_data.std()
csv_data.max()
csv_data.min()


# In[18]:


csv_data.median()


# In[19]:


csv_data.mode()


# In[20]:


csv_data.describe()


# In[23]:


csv_data.add(11) #Broadcasting -> 10 is added to all the values in the series


# In[26]:


csv_data + 11  #broadcasting 


# In[27]:


csv_data.sub(1)


# In[29]:


csv_data.mul(5) # can be written in this way too -> csv_data * 5 
csv_data.div(5) #can be written in  this way too -> csv_data / 5


# In[30]:


csv_data.value_counts() #this returns the count of times the index label appears 
#for example 1000.00 has appeared 26 times 


# In[35]:


csv_data.value_counts(ascending = True)
csv_data.value_counts(normalize= True) *100 #this is return the perecent of times the value occurs , 1000 appeared 2 percent


# In[37]:


#creating a fuhnction in python to take a parameter and then count the number of times 1 appear in it 
def count_of_one(number):
    return number.count(1)
count_of_one(111)


# In[38]:


def count_number_of_m(name):
    return name.count("m")
count_number_of_m("mahesh")


# In[45]:


csv_data= pd.read_csv("C:/Users/91749/Desktop/credit_risk_data.csv", usecols=["Employment_Status"]).squeeze("columns")
csv_data


# In[46]:


csv_data.apply(count_number_of_m)


# In[49]:


#Understanding Mapping Function properly 
job_status = {
    "Employed": 0,
    "Self-Employed":1
}


# In[51]:


csv_data.map(job_status) #for unemployed it is storing Nan a whit space


# In[ ]:




