#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#1.將下列清單(list1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")
a = np.array(range(30))
ra = a.reshape(5,6,order="F")
ra


# In[3]:


#2.呈上題的array，找出被6除餘1的數的索引
np.where(ra%6==1)


# In[ ]:




