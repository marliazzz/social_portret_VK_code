
import requests
from tqdm.notebook import tqdm
import pandas as pd
import time 

# Формируем универсальный url к VK API
url = 'https://api.vk.com/method/friends.get'

# Формируем параметры запроса к VK API
params = {'access_token':'ваш токен пользователя ВК', #токен пользователя берем с https://vk.com/dev/access_token?f=1.%20Ключ%20доступа%20пользователя
          'v':'5.131',
          'id':'-id пользователя, соц. портрет которого хотим создать', #id подаем через МИНУС, получаем id нужного нам пользователя через https://vk.com/linkapp
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
    params = {'access_token':'ваш токен пользователя ВК', #еще раз вставляем токен пользователя
          'v':'ваша версия ВК',#здесь указываем вашу версию ВК
          'user_id': ids,
          'extended':1,
          'fields':'description'}
    
    ind = requests.get(url, params = params).json()
    allgroup.append(ind)
    time.sleep(2)
    
resultat = []
for er in ind['response']['items']:
    resultat.append(er['description'])
resultat #получаем список групп друзей юзера с их описанием 
        







