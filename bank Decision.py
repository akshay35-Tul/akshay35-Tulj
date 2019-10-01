#!/usr/bin/env python
# coding: utf-8

# In[70]:


import pandas as pd


# In[71]:


import numpy as np


# In[72]:


from sklearn.model_selection import train_test_split


# In[73]:


us=pd.read_csv("E:\\akshay\\datasets\\bank.csv")


# In[74]:


us


# In[75]:


us.info()


# In[76]:


def score_to_numeric(x):
    if x=='yes':
        return 1
    if x=='no':
        return 0
us['deposit'] = us['deposit'].apply(score_to_numeric)


# In[77]:


def score_to_numeric(x):
    if x=='yes':
        return 1
    if x=='no':
        return 0
us['housing'] = us['housing'].apply(score_to_numeric)


# In[78]:


def score_to_numeric(x):
    if x=='yes':
        return 1
    if x=='no':
        return 0
us['loan'] = us['loan'].apply(score_to_numeric)


# In[79]:


us.head()


# In[80]:


X=us[['balance','housing','loan','campaign','age']]


# In[81]:


y=us[['deposit']]


# In[82]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3, random_state=0)


# In[83]:


from sklearn.tree import DecisionTreeClassifier


# In[84]:


lm=DecisionTreeClassifier(criterion='entropy', random_state=100, max_depth=3, min_samples_leaf=5)


# In[85]:


lm.fit(X_train, y_train)


# In[94]:


lm.predict(X_test)


# In[95]:


from sklearn import metrics


# In[96]:


print(metrics.accuracy_score(y_test, prediction))


# In[97]:


feature_cols=['balance','housing','loan','campaign','age']


# In[98]:


from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  
from IPython.display import Image  
import pydotplus



# In[ ]:




