#!/usr/bin/env python
# coding: utf-8

# In[3]:


marks = int(input("enter your marks: "))


# In[2]:


if (marks>50):
    if (marks>80):
        print("you have aced")
    elif (80>marks>70):
        print("grade B")
    else:
      print("congurtalation you have passed")
elif (marks==50):
    print("you just pass")
else:
    print("better luck next time")


# marks= 90
# 
# if (marks>50):
#     if (marks>80):
#         print("you have aced")
#     print("congurtalation you have passed")
# elif (marks==50):
#     print("you just pass")
# else:
#     print("better luck next time")

# In[13]:


a= 50


# In[14]:


type(a)


# In[15]:


float(a)


# # list

# In[1]:


a = ["kabeer",1,2,3,4,5,6,7,8,9]
print(a)


# In[2]:


print(a[0])


# In[4]:


print(a[5])


# In[20]:


print(a[6])


# In[21]:


print(a[0])


# In[5]:


print(a)


# In[6]:


print(a[::-1])


# In[7]:


print(a[1:5])


# In[8]:


print(a[0::2])


# # loops in python

# In[1]:


b = []
for _ in range(5):
    temp = input("Enter your value: ")
    b.append(temp)
print(b)


# In[4]:


k = []
for i in range(11):
   temp = input("enter your value:")
   k.append(temp)
print(k)


# In[12]:


c = []
for i in range(5):
    c.append(int(input("enter vak:")))
print(c)


# In[18]:


e =[]
for i in range(5):
  print("*"*e)


# In[19]:


for i in range(5):
    e.append("*")
    print("".join(e))


# In[23]:


e =[]
for i in range(5):
  print("*"*i)


# In[26]:


for i in range(10):
    int(input("enter any number:"))
    if(i==6):
       break


# In[35]:


a = input("enter your word")
if (a==a[::-1]):
        print("it is plandriom")
else:
        print("not a plandriom")


# In[ ]:




