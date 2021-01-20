#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[19]:


#1. 請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略?
english_score = np.array([55,89,76,65,48,70])

math_score = np.array([60,85,60,68,np.nan,60])

chinese_score = np.array([65,90,82,72,66,77])

ea=np.mean(english_score)
ma=np.nanmean(math_score)
ca=np.mean(chinese_score)

emax=np.amax(english_score)
mmax=np.nanmax(math_score)
cmax=np.amax(chinese_score)

emin=np.amin(english_score)
mmin=np.nanmin(math_score)
cmin=np.amin(chinese_score)

estd=np.std(english_score)
mstd=np.nanstd(math_score)
cstd=np.std(chinese_score)
print("英文","平均",ea,"最大值",emax,"最小值",emin,"標準差",estd)
print("數學","平均",ma,"最大值",mmax,"最小值",mmin,"標準差",mstd)
print("國文","平均",ca,"最大值",cmax,"最小值",cmin,"標準差",cstd)


# In[18]:


#2. 第五位同學補考數學後成績為55，請計算補考後數學成績平均、最大值、最小值、標準差?
math_score[4]=55
ma=np.mean(math_score)

mmax=np.amax(math_score)

mmin=np.amin(math_score)

mstd=np.std(math_score)
print("數學","平均",ma,"最大值",mmax,"最小值",mmin,"標準差",mstd)


# In[29]:


#3. 用補考後資料找出與國文成績相關係數最高的學科?
math_score[4]=55
ce=np.correlate(chinese_score, english_score)
cm=np.correlate(chinese_score, math_score)
if np.greater(ce,cm): 
    print("英文")
else:
    print("數學")


# In[ ]:




