#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from tqdm.notebook import tqdm
import pandas as pd
import time 

# Формируем универсальный url к VK API
url = 'https://api.vk.com/method/friends.get'

# Формируем параметры запроса к VK API
params = {'access_token':'ваш токен пользователя ВК',
          'v':'5.131',
          'id':'-id пользователя, соц. портрет которого хотим создать',
          'count':100,
          'offset':0}

# Формируем списки для сохранения данных
_friends = []

# Извелкаем и распределяем данные
for i in tqdm(range(0,130)):
    inf_friends = requests.get(url, params = params).json()
    for x in inf_friends:
        _friends.append(x)
        time.sleep(2)

_ids = inf_friends['response']['items']

allgroup = []

url = 'https://api.vk.com/method/groups.get' 
for ids in tqdm(_ids):
    params = {'access_token':'ваш токен пользователя ВК',
          'v':'ваша версия ВК',
          'user_id': ids,
          'extended':1,
          'fields':'description'}
    
    ind = requests.get(url, params = params).json()
    allgroup.append(ind)
    time.sleep(2)
    
resultat = []
for er in ind['response']['items']:
    resultat.append(er['description'])
resultat #получаем список группс их описанием друзей юзера
        


# In[ ]:




