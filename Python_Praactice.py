#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


list=["aditya","pranav","manuj"]


# In[3]:


series_data= pd.Series(list)


# In[4]:


series_data


# In[5]:


dictionary_one={"aditya":"good","pranav":"excellent","manuj":"outstanding"}


# In[6]:


print(dictionary_one.keys())


# In[7]:


print(dictionary_one.items())


# In[8]:


print(dictionary_one.values())


# In[9]:


dictionary_one.pop("aditya")


# In[10]:


dictionary_one


# In[11]:


dictionary_one["adi"]="good"


# In[12]:


dictionary_one


# In[13]:


dictionary_two={"aditya":3,"pranav":2,"manuj":1}


# In[14]:


dictionary_one.update(dictionary_two)


# In[15]:


dictionary_one


# In[16]:


dictionary_two


# In[19]:


dictionary_one.get("param","not found")


# In[20]:


len(dictionary_one)


# In[21]:


len(dictionary_two)


# In[22]:


grocery_list=[{"neem_powder":3,"jaggery":4,"biscuits":12},
             {"soap":12,"Good_night":1,"tooth_brush":2},]


# In[23]:


len(grocery_list)


# In[24]:


dictionary_grocery=grocery_list[1]


# In[25]:


dictionary_grocery


# In[27]:


dictionary_grocery=grocery_list[0]
dictionary_grocery


# In[28]:


grocery_list.append("pants")


# In[29]:


grocery_list


# In[32]:


grocery_list.insert(0,"This is the start of the list")


# In[33]:


grocery_list


# In[34]:


grocery_list.remove("This is the start of the list")


# In[35]:


grocery_list


# In[36]:


grocery_list.pop(0)


# In[37]:


grocery_list


# In[38]:


grocery_list[1]=["aditya"] #This is creating a list inside a list (nested)


# In[39]:


grocery_list


# In[41]:


grocery_list.append("me")


# In[42]:


grocery_list


# In[45]:


grocery_list[0:1]
grocery_list[:2]


# In[46]:


len(grocery_list)


# In[48]:


sushi={
    "salmon":"orange",
    "tuna":"red",
    "eel":"brown"
}


# In[49]:


pd.Series(sushi)


# In[62]:


prices = pd.Series([2.3,2.4,2.5])
prices
round(prices.sum(),2)
round(prices.product(),2)


# In[66]:


round(prices.mean(),2)
round(prices.std(),2) #It measures how spread out the values are from the mean (average)


# In[71]:


adjectives = pd.Series(["smart","handsome","charming","brilliant","smart"])
adjectives


# In[ ]:





# In[72]:


adjectives.is_unique


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




