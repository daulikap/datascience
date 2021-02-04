#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import library selenium
from selenium import webdriver


# In[2]:


# Buka browser chrome dan akses URL
driver=webdriver.Chrome('C:\Chromedriver\chromedriver')
driver.get("https://www.gojek.com")

# Menutup browser
driver.close()
print("URL successfully Accessed")


# In[ ]:




