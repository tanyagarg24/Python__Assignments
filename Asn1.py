
# coding: utf-8

# In[10]:


#insert an element into a list 
lst1 = [0,4,6,10]
lst1.insert(3,8)
print(lst1)  


# In[14]:


#sort a numeric list
lst1 = [1, 3, 4, 2,5,9,7] 
lst1.sort() 
  
print(lst1) 

#sort string list

lst2 =['1','3','4','2','5','9','7'] 
lst2.sort(key = int) 

print (str(lst2)) 

lst3= ['c', 'e', 'a', 'f','g','d'] 
lst3.sort() 
  
print(lst3) 


# In[17]:


#reverse a list
lst1=[3,4,5,6,7]
lst1.reverse()
print(lst1)

lst2=[3,4,5,6,7]
lst2r=lst2[::-1]
print(lst2r)


# In[28]:


#find common elements in list(integers)

lst1=[2,3,4,5]
lst2=[3,5,7,9]
lst3=[]
for x in lst1:
    if x in lst2:
        lst3.append(x)
        
#lst3 = [x for x in lst1 if x in lst2] 
print(lst3)


# In[27]:

#find common elements in list(strings)
lst1 = ['a','b','c'] 
lst2 = ['c','b','e'] 
lst3 =list(set(lst1)&set(lst2))
print(lst3)

