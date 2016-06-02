
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
get_ipython().magic(u'matplotlib inline')
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from glob import glob


# In[10]:

max_abusers = 1


# In[21]:

usage_report_names = glob('RhinoWeeklyUsageReport.*.csv')

master_df = None
for fname in usage_report_names:
    print fname
    date_str =  fname.split('.')[1]
    date_pd_obj = pd.to_datetime(date_str,format= '%Y%m%d')
    df = pd.read_csv(fname)
    df['date'] = date_pd_obj
    
    if master_df is None:
        master_df = df
    else:
        master_df = pd.concat([master_df,df], ignore_index=True)

# rt_idx = master_df.columns.index('RUNTUME (s)') 

# if rt_idx>=0:
columns = list(master_df.columns)

columns[1] = 'RUNTIME (s)'
master_df.columns=columns
        


# In[22]:

mean_usage_df = master_df.groupby('USER').mean()


# In[27]:

cpu_abusers  = mean_usage_df['CPUTIME (s)'].sort_values( ascending=False)
runtime_abusers = mean_usage_df['RUNTIME (s)'].sort_values(ascending=False)
memory_abusers = mean_usage_df['MEMORY (GB)'].sort_values(ascending=False)
io_abusers = mean_usage_df['IO (GB)'].sort_values( ascending=False)


# In[29]:

runtime_abusers.index


# In[ ]:




# In[ ]:




# In[40]:

runtime_abusers[:4].plot.pie(autopct='%.1f', fontsize=14, figsize=(6, 6), legend=True)

# rt = runtime_abusers[:max_abusers]

# labels = rt.index
# sizes = rt.values
# # colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
# # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

# plt.pie(sizes, 
# #         explode=explode, 
#         labels=labels, 
# #         colors=colors,
#         autopct='%1.1f%%', shadow=True, startangle=90)
# # Set aspect ratio to be equal so that pie is drawn as a circle.
# plt.axis('equal')
# plt.legend()


# In[41]:

cpu_abusers[:4].plot.pie(autopct='%.1f', fontsize=14, figsize=(6, 6), legend=True)


# In[42]:

io_abusers[:4].plot.pie(autopct='%.1f', fontsize=14, figsize=(6, 6), legend=True)


# In[43]:

memory_abusers[:4].plot.pie(autopct='%.1f', fontsize=14, figsize=(6, 6), legend=True)


# In[4]:

df = pd.read_csv('RhinoWeeklyUsageReport.20160531.csv')
df


# In[6]:

dt = 20160531
pd.to_datetime(dt,format= '%Y%m%d')


# In[7]:

df['date']=dt


# In[8]:

df


# In[ ]:



