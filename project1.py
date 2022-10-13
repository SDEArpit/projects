#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np 
import pandas as pd
import seaborn as sns
from scipy import stats


# In[2]:


df=pd.read_csv("https://raw.githubusercontent.com/Premalatha-success/July_10_HHE/main/hotel_bookings.csv")


# In[3]:


df.shape


# In[4]:


df.dtypes


# In[5]:


df.info


# In[6]:


df.isnull().sum()


# In[8]:


df.head()


# In[12]:


sns.catplot(x="hotel",y="lead_time",data=df)


# In[13]:


sns.catplot(x="hotel",y="lead_time",jitter=False,data=df)


# In[ ]:


sns.catplot(x="hotel",y="lead_time",kind="swarm",data=df)


# In[ ]:


df.sample(10)


# In[ ]:




