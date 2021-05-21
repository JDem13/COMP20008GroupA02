#!/usr/bin/env python
# coding: utf-8

# - income revenue vs school location   
# - income revenue vs school enrolments
# - income revenue vsclass sizes 

# # Load data

# In[1]:


url_enrolmens = 'http://www.education.vic.gov.au/Documents/about/research/datavic/dv297-govschoolatsienrollga2010-19.csv'
url_location = 'https://www.education.vic.gov.au/Documents/about/research/datavic/dv296-schoollocations2020.csv'
revenue_url = 'https://www.sro.vic.gov.au/ckfinder/userfiles/files/Payroll_Tax_Revenue_Collected%282%29.csv '
property_url = 'https://www.sro.vic.gov.au/ckfinder/userfiles/files/Land%20Tax_by_Municipality_2018.csv'
size_url = 'http://education.vic.gov.au/Documents/about/research/datavic/dv292-govschoolsclasssizesecondary2001-2019.csv'


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')


# In[3]:


enr_df = pd.read_csv(url_enrolmens, skiprows=2)
loc_df = pd.read_csv(url_location)
revn_df = pd.read_csv(revenue_url, skiprows=1, encoding='windows-1252')
property_df = pd.read_csv(property_url)
size_df = pd.read_csv(size_url)


# In[4]:


# loc_df


# ##  revenue

# In[5]:


revn_df['Year'] = revn_df['Year'].apply(lambda x: "20"  + str(x).split("/")[1]).astype(int)
revn_df['Revenue']= revn_df['Revenue ($ million)'].apply(lambda x: str(x).replace(',', '')).astype(float)
revn_df.head()


# ## enrolment

# In[6]:


enr_df_id = enr_df.set_index('LGA', drop= True)
enr_df_total = enr_df_id.loc['Grand Total',:].apply(lambda x: str(x).replace(',', '')).astype(float)
enr_df_total


# ##  class size

# In[7]:


size_t = size_df.set_index('Secondary English Classes').T
size_t


# In[8]:


revn_df['enrolment'] = [np.nan] * 9 + enr_df_total.to_list()
revn_df.index = revn_df.Year
revn_df['Average class size Year 12'] = size_t['Average class size Year 12'].to_list()
revn_df['Average class size-all classes'] = size_t['Average class size-all classes'].to_list()
revn_df = revn_df.iloc[:, 2:]
revn_df


# In[9]:


revn_df.describe()


# # Analysis

# ##  revenue vs school enrolments

# In[10]:


revn_df[['Revenue', 'enrolment']].plot(figsize = (8, 6))
plt.title('time series : revenue and enrolment')
plt.show()


# In[11]:


revn_df.plot.scatter(x = 'Revenue', y = 'enrolment', figsize = (8, 6))
plt.title('relation between Revenue and Enrolment')
plt.show()


# In[12]:


import statsmodels.api as sm
X = revn_df[['Revenue', 'enrolment']].copy().dropna()
print(X.corr())
Y = X.pop('enrolment')
X = sm.add_constant(X) # adding a constant
model = sm.OLS(Y, X).fit()
res = model.summary()
print(res)


# ## revenue vs school calss size

# In[13]:


revn_df[['Average class size Year 12', 'Average class size-all classes']].plot(figsize = (8, 6))
plt.title('time series : class size')
plt.show()


# In[14]:


ax = plt.subplot(1, 2 ,1 )
revn_df.plot.scatter(x = 'Revenue', y ='Average class size Year 12', figsize = (16, 6), ax = ax)
plt.title('relation between Revenue and class size Year 12(average)')
import numpy as np
ax = plt.subplot(1, 2 ,2 )
revn_df['log_revenue'] =  np.log(revn_df['Revenue'] )
revn_df.plot.scatter(x = 'log_revenue', y ='Average class size Year 12', figsize = (16, 6), ax = ax)
plt.title('relation between Revenue and class size Year 12(average, log)')
plt.show()


# In[ ]:





# In[15]:


revn_df[['Revenue', 'Average class size Year 12','log_revenue']].corr()[['Average class size Year 12']]


# In[16]:


X = revn_df[['log_revenue', 'Average class size Year 12']].copy().dropna()
Y = X.pop('Average class size Year 12')
X = sm.add_constant(X) # adding a constant
model = sm.OLS(Y, X).fit()
res = model.summary()
print(res)


# In[17]:


revn_df.plot.scatter(x = 'Revenue', y ='Average class size-all classes', figsize = (8, 6))
plt.title('relation between Revenue and Average class size-all classes')
plt.show()


# In[18]:


X = revn_df[['Revenue', 'Average class size-all classes']].copy().dropna()
print(X.corr())
Y = X.pop('Average class size-all classes')
X = sm.add_constant(X) # adding a constant
model = sm.OLS(Y, X).fit()
res = model.summary()
print(res)


# In[ ]:




