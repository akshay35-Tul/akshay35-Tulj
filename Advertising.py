#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


from sklearn.model_selection import train_test_split


# In[4]:


adv=pd.read_csv("E:\\akshay\\datasets\\Advertising.csv")


# In[5]:


adv.head()


# In[9]:


def myFunction(myData):
    col = [[0,0],[0,0],[0,0]]
    for i in range(len(tableData)):
        for word in tableData[i]:
            if len(word) > col[i][1]:
                col[i][1]=word
        print(col[i][1])


# In[12]:


def score_to_numeric(x):
    if x<17:
        return 0
    if x<27:
        return 1
adv['Sales'] = adv['Sales'].apply(score_to_numeric)


# In[13]:


adv


# In[14]:


adv.dropna(inplace=True)


# In[15]:


adv


# In[17]:


from sklearn.tree import DecisionTreeClassifier


# In[18]:


X=adv[["TV","Radio","Newspaper"]]


# In[19]:


y=adv[["Sales"]]


# In[20]:


from sklearn.model_selection import train_test_split


# In[21]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3, random_state=0)


# In[23]:


lm=DecisionTreeClassifier(criterion='gini', random_state=100, max_depth=3, min_samples_leaf=3)


# In[24]:


lm.fit(X_train, y_train)


# In[25]:


prediction=lm.predict(X_test)


# In[27]:


from sklearn import metrics


# In[28]:


print(metrics.accuracy_score(y_test, prediction))


# In[30]:


lm1=DecisionTreeClassifier(criterion='entropy', random_state=100, max_depth=3, min_samples_leaf=3)


# In[31]:


lm1.fit(X_train,y_train)


# In[32]:


prediction=lm1.predict(X_test)


# In[33]:


feature_cols=["TV","Radio","Newspaper"]


# In[34]:



from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  
from IPython.display import Image  
import pydotplus


# In[35]:


dot_data = StringIO()
export_graphviz(lm1, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('diabetes.png')
Image(graph.create_png())



# In[ ]:




