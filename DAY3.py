#!/usr/bin/env python
# coding: utf-8

# # Take last 3 values of roll number If the value startswith "01" ---> "Cse dept" elif the value startswith "11" ---> "It dept" elif the value startswith "21" ---> "Ece dept" else not a student of Srm University
# 

# In[ ]:





# In[ ]:





# In[12]:



a=input("EnterRoll No ")

if a[-3:].startswith("01"):
    print("You belong to CSE Dept.")
elif a[-3:].startswith("11"):
    print("You belong to IT Dept.")
elif a[-3:].startswith("21"):
    print("You belong to ECE Dept.")
else:
    print("You are not an SRM student.")


# # Find all leap years between 1800 to 2020

# In[17]:


for i in range(1800,2020):
    if ((i%4==0 or i%400==0) and (i%100!=0)):
        print(i,end="   ")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




