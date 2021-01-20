#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#1.將下列清單(list1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")
array1 = np.array(range(30))
array1.reshape((5, 6))


# In[4]:


#2.呈上題的array，找出被6除餘1的數的索引
np.where(array1%6==1)

