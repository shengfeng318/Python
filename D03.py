#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#1.正常的談話的聲壓為20000微巴斯卡，請問多少分貝?
#請寫下程式
V1 = 20000
V0 = 20
GdB=20*(np.log10(V1/V0))
print(GdB)


# In[46]:


#2.30分貝的聲壓會是50分貝的幾倍?
#公式移項過後可以得到 V1 = ?
#請寫下程式
V50=np.power(10, 2.5)*20
V30=np.power(10, 1.5)*20
print(np.rint(V50/V30))

