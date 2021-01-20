#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[7]:


#1. 請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略?
english_score = np.array([55,89,76,65,48,70])

math_score = np.array([60,85,60,68,np.nan,60])

chinese_score = np.array([65,90,82,72,66,77])

ea=np.mean(english_score)
ma=np.nanmean(math_score)
ca=np.mean(chinese_score)
print(ea,ma,ca)

emax=np.amax(english_score)
mmax=np.nanmax(math_score)
cmax=np.amax(chinese_score)
print(emax,mmax,cmax)

emin=np.amin(english_score)
mmin=np.nanmin(math_score)
cmin=np.amin(chinese_score)
print(emin,mmin,cmin)

estd=np.std(english_score)
mstd=np.nanstd(math_score)
cstd=np.std(chinese_score)
print(estd, mstd,cstd)


# In[8]:


#2. 第五位同學補考數學後成績為55，請計算補考後數學成績平均、最大值、最小值、標準差?
math_score[4]=55
ma=np.mean(math_score)
print(ma)

mmax=np.amax(math_score)
print(mmax)

mmin=np.amin(math_score)
print(mmin)

mstd=np.std(math_score)
print(mstd)


# In[15]:


#3. 用補考後資料找出與國文成績相關係數最高的學科?
ce=np.correlate(chinese_score, english_score)
cm=np.correlate(chinese_score, math_score)
a=np.greater(ce,cm)
if a==1:print("english")
else:print("math")

