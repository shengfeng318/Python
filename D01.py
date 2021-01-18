#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[6]:


#1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。
a=np.linspace(0,20, num=21, endpoint=True)
a


# In[8]:


#2.呈上題，將以上數列取出偶數。
a[0:21:2]


# In[9]:


#3.呈1題，將數列取出3的倍數。
a[0:21:3]


# In[ ]:




