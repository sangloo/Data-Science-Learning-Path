
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

data = pd.read_csv('C:\\Users\\Kirill\\Desktop\\Workshop005\\Students_Data.csv')


# In[3]:

data.head()


# In[7]:

data.columns = ["Gender", "Nationality", "PlaceOfBirth", "StageID", "SectionID", "GradeID", "Topic", "Semester", "Relation", "RaisedHands", "VisitedResources", "AnnouncementsView", "Discussion", "ParentAnsweringSurvey", "ParentSchoolSatisfaction", "StudentAbsenceDays", "Class"]


# In[9]:

data.head()


# In[10]:

set(data["Nationality"])


# In[13]:

data["Nationality"] = data["Nationality"].replace("KW","Kuwait")


# In[14]:

data["Nationality"] = data["Nationality"].replace("SaudiArabia","Saudi Arabia")


# In[15]:

data["Nationality"] = data["Nationality"].replace("lebanon","Lebanon")


# In[16]:

data["Nationality"] = data["Nationality"].replace("venzuela","Venezuela")


# In[17]:

set(data["Nationality"])


# In[18]:

set(data["Class"])


# In[20]:

set(data["StageID"])


# In[22]:

data["StageID"] = data["StageID"].replace("lowerlevel","LowerLevel")


# In[23]:

set(data["StageID"])


# In[24]:

# --------------------------


# In[32]:

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[28]:

data.head()


# In[29]:

data.info()


# In[34]:

#allocation by class
plt.figure(figsize = (20,10))
sns.countplot(x="Topic", data=data)
plt.show()


# In[35]:

#allocation by country
plt.figure(figsize = (20,10))
sns.countplot(x="Nationality", data=data)
plt.show()


# In[41]:

#Student performance
plt.figure(figsize = (20,10))
sns.countplot(x="Class", data=data, palette='PuBu', order=['L','M','H'])
plt.show()


# In[42]:

#boys vs girls
plt.figure(figsize = (20,10))
sns.countplot(x="Gender", data=data, palette='PuBu', hue='Class', hue_order=['L','M','H'])
plt.show()




# In[44]:

#performance ~ attendance
plt.figure(figsize = (20,10))
sns.countplot(x="StudentAbsenceDays", data=data, palette='PuBu', hue='Class', hue_order=['L','M','H'])
plt.show()



# In[48]:

#attendance ~ parents satisfaction
plt.figure(figsize = (20,10))
sns.countplot(x="ParentSchoolSatisfaction", data=data, hue='StudentAbsenceDays')
plt.show()



# In[51]:

#performance ~ attendance
plt.figure(figsize = (20,10))
sns.barplot(x='Class', y='RaisedHands', data=data, order=['L','M','H'])
plt.show()


