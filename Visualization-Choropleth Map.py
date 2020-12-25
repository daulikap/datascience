#!/usr/bin/env python
# coding: utf-8

# # Data Visualization - Choropleth Map 

# 1. Import Library

# In[1]:


import json
import pandas as pd
import requests
import folium
import numpy as np


# 2. Load GeoJSON West Java Map

# In[2]:


jabar_geo=json.load(open(r"C:\Users\daulika pratiwi\Downloads\jds\kota.geojson"))


# In[4]:


jabar_geo['features'][0]['properties'].keys()


# 3. Load spread of COVID-19 cases data in Jawa Barat

# In[3]:


jabar_json=requests.get('https://covid19-public.digitalservice.id/api/v1/sebaran_v2/jabar').json()


# In[5]:


jabar_json.keys()


# In[13]:


jabar_data=jabar_json['data']['content']


# In[7]:


jabar_data=pd.DataFrame(jabar_data)
jabar_data.head()


# 3. Count spread cases based on Kode Kabupaten

# In[8]:


jabar_count=jabar_data.groupby(['kode_kab']).size().reset_index(name='counts')
jabar_count


# 4. Load West Java Map with Folium 

# In[10]:


peta_jabar= folium.Map(location=[-6.867350, 107.604332], zoom_start=8)
peta_jabar


# 5. Define and display Choropleth Map with Folium

# In[11]:


peta_jabar.choropleth(
    geo_data=jabar_geo,
    data=jabar_count,
    columns=['kode_kab','counts'],
    key_on='feature.properties.bps_kode',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Sebaran Kasus COVID-19 Jawa Barat'
)

peta_jabar


# In[ ]:




