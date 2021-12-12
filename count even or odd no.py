#!/usr/bin/env python
# coding: utf-8

# In[29]:



numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for value in numbers:
    if (not value % 2):
            even+=1
    else:
            odd+=1  
            
print("Number of even numbers : ",even)
print("Number of odd numbers : ",odd)


# In[1]:



numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for value in numbers:
    if (not value % 2):
            odd+=1
    else:
            even+=1  
            
print("Number of even numbers : ",even)
print("Number of odd numbers : ",odd)

