#!/usr/bin/env python
# coding: utf-8

# In[2]:


def mean_value(*n):
    sum = 0
    counter = 0
    for x in n:
        counter = counter + 1
        sum +=x


# In[4]:


def median_value(*n):
    num_list = list(n)
    num_list.sort()
    l = len(num_list)
    if l%2 == 0:
        median = (num_list[int(l/2)] + num_list[int((l/2))-1])/2
    else:
        median = num_list[int(l/2)]
    return median


# In[8]:


median_value(10,30,45,56,78,99)


# In[ ]:




