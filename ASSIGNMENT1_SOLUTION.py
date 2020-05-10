#!/usr/bin/env python
# coding: utf-8

# # Objects and Data Structures Assessment Test

# ## Test your knowledge. 
# 
# ** Answer the following questions **

# Write a brief description of all the following Object Types and Data Structures we've learned about: 

# Numbers: these can be of 2 types: 1.integers eg. 1,2,3,45  2.float eg. 12.23,56.45,89.78
# 
# Strings: these are texts written in inverted commas eg. "hello world"
# 
# Lists: these are a array of strings, numbers written in square brackets and are mutable.
# 
# Tuples: these are immutable and are kept in paranthesis. can be strings and numbers as well.
# 
# Dictionaries: these are values denoted to a variable separated by semicolon in curly brackets and can be strings as well as numbers.
# 

# ## Numbers
# 
# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
# 
# Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

# In[12]:


print(((5*4)**2+2-1)/4)


# Answer these 3 questions without typing code. Then type code to check your answer.
# 
#     What is the value of the expression 4 * (6 + 5)
#     
#     What is the value of the expression 4 * 6 + 5 
#     
#     What is the value of the expression 4 + 6 * 5 

# In[12]:


# 4*(6+5)=44
a=4*(6+5)
print(a)


# In[13]:


# 4*6+5=29
b=4*6+5
print(b)


# In[14]:


# 4+6*5=34
c=4+6*5
print(c)


# What is the *type* of the result of the expression 3 + 1.5 + 4?<br><br>

# What would you use to find a number’s square root, as well as its square? 

# In[9]:


# Square root:
a=45**(1/2)
print(a)


# In[11]:


# Square:
b=45**2
print(b)


# ## Strings

# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

# In[2]:


s = 'hello'
# Print out 'e' using indexing
print(s[1])


# Reverse the string 'hello' using slicing:

# In[3]:


s ='hello'
# Reverse the string using slicing
print(s[::-1])


# Given the string hello, give two methods of producing the letter 'o' using indexing.

# In[4]:


s ='hello'
# Print out the 'o'

# Method 1:
print(s[4])


# In[6]:


# Method 2:
print(s[4:])


# ## Lists

# Build this list [0,0,0] two separate ways.

# In[21]:


# Method 1:
l=[0]*3
l


# In[22]:


# Method 2:
a=[0]
a+a+a


# Reassign 'hello' in this nested list to say 'goodbye' instead:

# In[37]:


list3 = [1,2,[3,4,'hello']]
list3.pop()
print(list3)


# In[38]:


list3.append([3,4,'goodbye'])
print(list3)


# Sort the list below:

# In[27]:


list4 = [5,3,4,6,1]
sorted_list=sorted(list4)
print(sorted_list)
print(list4)


# ## Dictionaries

# Using keys and indexing, grab the 'hello' from the following dictionaries:

# In[43]:


d = {'simple_key':'hello'}
# Grab 'hello'
d['simple_key']


# In[46]:


d = {'k1':{'k2':'hello'}}
# Grab 'hello'
d['k1']['k2']


# In[57]:


# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello
d['k1'][0]['nest_key'][1][0]


# In[62]:


d={"k1":[{'super':'annoying','final':{"chi":"forget","key":[123,{"left":[123,"hello"]}]}}],"second":{"finally":123}}
d['k1'][0]['final']['key'][1]['left'][1]


# In[63]:


# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
d['k1'][2]['k2'][1]['tough'][2][0]


# Can you sort a dictionary? Why or why not?<br><br>

# ## Tuples

# What is the major difference between tuples and lists?
# ans-tuples are immutable whereas lists are mutable.

# How do you create a tuple?
# ans- 

# In[64]:


a=(1,4,67,'srishti',45.98,[34,'hello'],{'k1':43.21,'k2':'world'})


# In[65]:


a


# ## Sets 

# What is unique about a set?
# basically its a list but it does not allow duplicates.

# Use a set to find the unique values of the list below:

# In[68]:


list5 = [1,2,2,33,4,4,11,22,3,3,2]
set1={1,2,2,33,4,4,11,22,3,3,2}
set1


# In[75]:


set2={'sreekar','srishti','gargi','avni','ajay','alka', 3, 8, 63, 62}
set2


# ## Booleans

# For the following quiz questions, we will get a preview of comparison operators. In the table below, a=3 and b=4.
# 
# <table class="table table-bordered">
# <tr>
# <th style="width:10%">Operator</th><th style="width:45%">Description</th><th>Example</th>
# </tr>
# <tr>
# <td>==</td>
# <td>If the values of two operands are equal, then the condition becomes true.</td>
# <td> (a == b) is not true.</td>
# </tr>
# <tr>
# <td>!=</td>
# <td>If values of two operands are not equal, then condition becomes true.</td>
# <td> (a != b) is true.</td>
# </tr>
# <tr>
# <td>&gt;</td>
# <td>If the value of left operand is greater than the value of right operand, then condition becomes true.</td>
# <td> (a &gt; b) is not true.</td>
# </tr>
# <tr>
# <td>&lt;</td>
# <td>If the value of left operand is less than the value of right operand, then condition becomes true.</td>
# <td> (a &lt; b) is true.</td>
# </tr>
# <tr>
# <td>&gt;=</td>
# <td>If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.</td>
# <td> (a &gt;= b) is not true. </td>
# </tr>
# <tr>
# <td>&lt;=</td>
# <td>If the value of left operand is less than or equal to the value of right operand, then condition becomes true.</td>
# <td> (a &lt;= b) is true. </td>
# </tr>
# </table>

# What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# In[76]:


# Answer before running cell
2 > 3 #False


# In[77]:


# Answer before running cell
3 <= 2 #False


# In[78]:


# Answer before running cell
3 == 2.0 #False


# In[80]:


# Answer before running cell
3.0 == 3 #True


# In[81]:


# Answer before running cell
4**0.5 != 2 #False


# Final Question: What is the boolean output of the cell block below?

# In[83]:


# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1'] #False


# ## Great Job on your first assessment! 
