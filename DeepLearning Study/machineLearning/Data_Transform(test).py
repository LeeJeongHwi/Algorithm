#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


marathon_2017 = pd.read_csv("./boston-results/marathon_results_2017.csv")


# In[3]:


print(marathon_2017.head())


# In[4]:


print(marathon_2017.info())


# In[5]:


#긱 Column의 Null 값의 갯수 합
marathon_2017.isnull().sum(axis=0)


# In[6]:


marathon_2017.columns


# In[7]:


#Column Data 정제


# In[8]:


marathon_2017_clean = marathon_2017.drop(['Unnamed: 0','Bib','Unnamed: 9'],axis='columns')


# In[9]:


marathon_2017_clean.head()


# In[10]:


marathon_2017_clean.info()


# In[11]:


#Column Data 추가


# In[12]:


marathon_2017_clean['Senior'] = marathon_2017_clean.Age > 60


# In[13]:


marathon_2017_clean.head()


# In[14]:


marathon_2017_clean["Year"] = '2017'


# In[15]:


print(marathon_2017_clean.info())


# In[16]:


#데이터 선택


# In[17]:


names = marathon_2017_clean.Name
print(names)


# In[18]:


official_time = marathon_2017_clean["Official Time"]
print(official_time)


# In[19]:


#데이터 조건 선택


# In[20]:


print(marathon_2017_clean.info())


# In[21]:


seniors = marathon_2017_clean.Age > 60


# In[22]:


print(seniors)


# In[23]:


KEN_runner = marathon_2017_clean[marathon_2017_clean.Country == 'KEN']


# In[24]:


print(KEN_runner)


# In[25]:


#데이터변환


# In[26]:


print(marathon_2017_clean.head())


# In[27]:


#Official Time 을 초로 변환하기
def toSeconds(record):
    hms = record.str.split(":",n=2,expand = True)
    return hms[0].astype(int)*3600 + hms[1].astype(int)*60 + hms[2].astype(int)

marathon_2017['Official Time Sec'] = toSeconds(marathon_2017['Official Time'])


# In[28]:


print(marathon_2017.head())


# In[29]:


import numpy as np
#pd.to_timedelta == 시간을 초로 변환하는 것


# In[30]:


marathon_2017['Official Time Sec'] = pd.to_timedelta(marathon_2017['Official Time'])
marathon_2017['Official Time New'] = marathon_2017['Official Time Sec'].astype("m8[s]").astype(np.int64)


# In[31]:


print(marathon_2017.head())


# In[32]:


#데이터 저장
marathon_2015 = pd.read_csv("./boston-results/marathon_results_2015.csv")
marathon_2016 = pd.read_csv("./boston-results/marathon_results_2016.csv")
marathon_2017 = pd.read_csv("./boston-results/marathon_results_2017.csv")
#concat => []에 있는 데이터프레임을 하나로 뭉침
marathon_2015_2017 = pd.concat([marathon_2015,marathon_2016,marathon_2017], ignore_index=True,sort=False).set_index("Official Time")
#descirbe ==> 4분위수,mean,std,min,max (R에선 Summary()랑 같음)
print(marathon_2015_2017.describe())


# In[33]:


marathon_2015_2017.sort_values(by=['Age'],ascending=False)
#ascending 매개변수는 오름차순 , 내림차순(default = True)


# In[34]:


#save to Csv 
marathon_2015_2017.to_csv('./boston-results/marathon_2015_2017.csv',index=None,header=True)


# In[35]:


print(marathon_2015_2017.info())

