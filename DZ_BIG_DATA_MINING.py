import requests
from pprint import pprint
import json
# req = requests.get('http://www.mail.ru')
# main_link = 'https://api.openweathermap.org/data/2.5/weather'
# city = 'Barcelona'
# appid = 'b76056c6e9921e016036ea860920f2e6'
# req = requests.get(f'{main_link}?q={city}&appid={appid}')
# if req.ok:
#     data = json.loads(req.text)
#     print(f"Р’ РіРѕСЂРѕРґРµ {data['name']} С‚РµРјРїРµСЂР°С‚СѓСЂР° {data['main']['temp']-273.15} РіСЂР°РґСѓСЃРѕРІ")
### ЗАДАЧА ВЫВЕСТИ СПИСОК РеПозиториев
name = 'bigdatacon'
r = requests.get('https://api.github.com/users/name/repos')

if r.ok:
    data = json.loads(r.text)
    pprint(data)

#### Задача залогиниться на гитхаб
username = 'bigdatacon'
password = 'zvol1503'
reg = requests.get('https://api.github.com/user', auth=(username, password))
data2 = json.loads(reg.text)
pprint(data2)


#### ЗАДАЧА ЗАЛОГИНИТЬСЯ ЧЕРЕЗ CURL (Логинился на гикбрейнс и гитхаб, код ниже, скриншоты в отдельном файле)
# curl -v -u postman:password https://postman-echo.com/basic-auth

# curl -v -u <vin17@list.ru:link1789> https://geekbrains.ru/login
# curl -v -u bigdatacon:zvol1503 https://github.com/login

#### ВОПРОС, почему при обеих попытказ залогинииться, ответ сервера 200, и в конце надпись left intact, но нет надписи что
### authorized: true???


