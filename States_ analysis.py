#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
df=pd.read_csv("state_data.csv")
df


# In[6]:


df.info()


# In[31]:


df.isnull().sum()


# In[7]:


df.describe()


# In[25]:


df.head(14)


# In[26]:


df.tail(14)


# In[4]:


df['Population'].describe()


# In[8]:


df['Population'].count()


# In[9]:


df['Population'].min()


# In[10]:


df['Population'].max()


# In[56]:


df['Literacy rate'].describe()


# In[58]:


df['Literacy rate'].count()


# In[59]:


df['Literacy rate'].min()


# In[60]:


df['Literacy rate'].max()


# In[61]:


df['Total crime'].describe()


# In[62]:


df['Total crime'].count()


# In[63]:


df['Total crime'].min()


# In[64]:


df['Total crime'].max()


# In[65]:


df['Area'].describe()


# In[66]:


df['Area'].count()


# In[67]:


df['Area'].min()


# In[68]:


df['Area'].max()


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:





# In[21]:


plt.boxplot(df['Population'])
plt.title('Population')
plt.show()


# In[69]:


plt.hist(df['Population'])
plt.title('Populations Histogram')
plt.xlabel("Population")
plt.ylabel("State/UT")
plt.show()


# In[34]:


plt.violinplot(df['Population'])


# In[43]:


x=df['Population']
y=df['State/UT']
plt.scatter(x,y)
plt.xlabel('Population')
plt.ylabel('State/UT')
plt.show()


# In[36]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[50]:


import seaborn as sns
Stateds=pd.read_csv("state_data.csv")
Stateds


# In[51]:


sns.swarmplot(x='Population', y='State/UT', data=Stateds)


# In[52]:


sns.countplot(Stateds['Population'])


# In[53]:


Stateds['Population'].value_counts()


# In[54]:


sns.histplot(data=Stateds, x='Population')


# In[ ]:




