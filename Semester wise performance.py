#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv(r"C:\Users\devan\Downloads\Stud_result.csv")


# In[3]:


df


# In[31]:


semwise=df.groupby(['Sem','Gender','Batch'])


# In[32]:


semwise.get_group((3,'M','A'))


# In[34]:


semwise.get_group((5,'F','C'))


# In[35]:


semwise.get_group((5,'M','A')).min()


# In[14]:


semwise.mean()


# In[19]:


semwise.max()


# In[22]:


semwise.min()


# In[23]:


semwise.sum()


# In[24]:





# In[36]:


df=pd.read_csv(r"C:\Users\devan\Downloads\Stud_result.csv")


# In[37]:


df


# In[1]:


df['add']=df.apply(lambda x:' Sub1'+ 'Sub2' + 'Sub3')         


# In[51]:


df


# In[42]:


df['status']=df['add'].transform(lambda x:'GOOD' if (x>100) else 'BAD')


# In[43]:


df


# In[56]:


print(df.iloc[: ,0:3])


# In[62]:


print(df.loc[['Sem:Batch'],'0':'5'])


# In[ ]:




