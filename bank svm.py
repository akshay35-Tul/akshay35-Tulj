#!/usr/bin/env python
# coding: utf-8

# In[115]:


import pandas as pd


# In[116]:


import numpy as np


# In[117]:


from sklearn.model_selection import train_test_split


# In[118]:


us=pd.read_csv("E:\\akshay\\datasets\\bank.csv")


# In[119]:


us.head()


# In[120]:


us.info()


# In[121]:


def score_to_numeric(x):
    if x=='yes':
        return 1
    if x=='no':
        return 0
us['deposit'] = us['deposit'].apply(score_to_numeric)


# In[122]:


def score_to_numeric(x):
    if x=='yes':
        return 1
    if x=='no':
        return 0
us['housing'] = us['housing'].apply(score_to_numeric)


# In[123]:


def score_to_numeric(x):
    if x=='yes':
        return 1
    if x=='no':
        return 0
us['loan'] = us['loan'].apply(score_to_numeric)


# In[124]:


def score_to_numeric(x):
    if x=='primary':
        return 1
    if x=='secondary':
        return 2
    if x=='tertiary':
        return 3
    if x=='unknown':
        return 4
    
    
        
    
    
    
    
    
us['education'] = us['education'].apply(score_to_numeric)



# In[125]:



def score_to_numeric(x):
    if x=='married':
        return 1
    if x=='single':
        return 2
    if x=='blue-collar':
        return 3
    if x=='divorced':
        return 4
    
    
        
    
    
    
    
    
us['marital'] = us['marital'].apply(score_to_numeric)



# In[126]:


def score_to_numeric(x):
    if x=='management':
        return 1
    if x=='technician':
        return 2
    if x=='blue-collar':
        return 3
    if x=='admin.':
        return 4
    if x=='services':
        return 5
    if x=='11th':
        return 6
    if x=='retired':
        return 7
    if x=='self-employed':
        return 8
    if x=='unemployed':
        return 9
    if x=='entrepreneur':
        return 10
    if x=='housemaid':
        return 11
    if x=='unknown':
        return 12
   
    
    
    
    
    
        
    
    
    
    
    
us['job'] = us['job'].apply(score_to_numeric)



# In[127]:


us.head()


# In[128]:



X=us[['job','marital','education','balance']]



# In[129]:



y=us[['deposit']]




# In[130]:


from sklearn.model_selection import train_test_split


# In[131]:


X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.3, random_state=0)


# In[132]:


X_train = X_train.fillna(X_train.mean())


# In[133]:


y_train = y_train.fillna(y_train.mean())


# In[134]:


from sklearn import svm


# In[135]:


lm=svm.SVC(kernel='linear')


# In[ ]:


lm.fit(X_train, y_train)


# In[ ]:


from sklearn import metrics


# In[ ]:


prediction=lm.predict(X_test)


# In[ ]:


print(metrics.accuracy_score(y_test, prediction))


# In[ ]:




