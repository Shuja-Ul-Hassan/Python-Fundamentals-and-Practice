#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[3]:


#Task 1: Basic Creation and Access
my_info=('Shuja',18,1.7272)
print(my_info)
print(my_info[1])


# In[10]:


#Task 2: Single-Item Tuple
single_day=('Monday',)
print(type(single_day))


# In[7]:


#Task 3: Negative Indexing
planets=('Mercury','Venus','Earth','Mars','Jupiter')
print(planets[-1])
print(planets[2])


# In[8]:


#Task 4: Tuple Concatenation
front_numbers=(1,2,3)
back_numbers=(4,5,6)
combined_numbers=front_numbers+back_numbers
print(combined_numbers)


# In[9]:


#Task 5: Tuple Repetition
icon=('⭐',)
ratings=icon*3
print(ratings)


# In[11]:


#Task 6: The Immutability Test
status=('pending','processing','completed')
status[0]='failed'
#type_error occurs because the tuple cannot be modified


# In[15]:


#Task 7: Tuple Slicing
data=(10,20,30,40,50,60,70)
print(data[2:5])
print(data[0:4])


# In[17]:


#Task 8: Counting Elements
results=('pass','fail','pass','pass','defer','pass')
print(results.count('pass'))
print(results.index('defer'))
