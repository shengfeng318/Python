#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[6]:


#1.有多少學生英文成績比數學成績高?
english_score = np.array([55,89,76,65,48,70])

math_score = np.array([60,85,60,68,55,60])

chinese_score = np.array([65,90,82,72,66,77])

n=np.greater(english_score, math_score)
print(np.sum(n))


# In[17]:


#2.是否全班同學最高分都是國文?
n1=np.greater(chinese_score, math_score)
n2=np.greater(chinese_score, english_score)
cm=np.all(n1)
ce=np.all(n2)
np.logical_and(cm, ce)

