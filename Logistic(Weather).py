#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd


# In[21]:


import numpy as np


# In[22]:


from sklearn.model_selection import train_test_split


# In[55]:


df=pd.read_csv("E:\\akshay\\datasets\\weather.csv")


# In[56]:


df.head()


# In[57]:


df.info()


# In[58]:



#Convert A String Categorical Variable To A Numeric Variable
def score_to_numeric(x):
    if x=='Yes':
        return 1
    if x=='No':
        return 0
    


# In[60]:


df['RainToday1'] = df['RainToday'].apply(score_to_numeric)


# In[61]:


df.head()


# In[62]:


X=df[["Cloud3pm","Temp3pm"]]


# In[63]:


y=df[["RainToday1"]]


# In[64]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3, random_state=0)


# In[65]:


from sklearn.linear_model import LogisticRegression


# In[66]:


lm=LogisticRegression()


# In[67]:


lm.fit(X_train, y_train)


# In[68]:


prediction=lm.predict(X_test)


# In[69]:


from sklearn import metrics


# In[70]:


print(metrics.accuracy_score(y_test, prediction))


# In[ ]:




