#!/usr/bin/env python
# coding: utf-8

# In[11]:


def remove_punc(input_text):
    punctuation_marks = ['.',',','!','?',';','(',')',':','^','{','+','-','<','>','"',]
    output_text = ""
    for char in input_text:
        if char not in punctuation_marks:
            output_text += char
    return output_text


# In[13]:


remove_punc('''Hello!, "How are you?"''')


# In[17]:


def remove_stopwords(input_text):
    stop_words = ["is", "and", "the", "a", "an", "in", "on", "can", "by", "why", "ok"]
    words = input_text.split()
    filtered_words = []
    for word in words:
        if word.lower() not in stop_words:
            filtered_words.append(word)
    output_text = ' '.join(filtered_words)
    return (output_text)


# In[21]:


remove_stopwords('''we can make a good movie and have an juice''')


# In[ ]:




