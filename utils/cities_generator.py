import yaml, sys, requests
sys.path.append("..")
from config.global_config import API_key, URL_geo
from utils.cities_reader import Cities

def write_cities(city_list):
    with open('../config/cities.yaml', 'w') as file:
        yaml.dump(city_list, file)

def see_list(listdata):
    for i in range(len(listdata)):
        print (f'{str(i)}. {str(listdata[i])}')


def set_list():
    city_list = Cities.get_cities_list('../config/cities.yaml')
    if city_list == 'Fail':
        return 'Fail'
    see_list(city_list)
    req = ''
    while req != 'F' and req != 'f':
        req = str(input('Введите F для сохранения списка, A добавить элемент, D удалить: '))
        if req == 'A' or req == 'a':
            newcity = str(input('Введите название города для добавления (на английском), либо X для отмены: '))
            if newcity == 'X' or newcity == 'x': continue
            geo_URL = f'{str(URL_geo)}?q={newcity}&appid={str(API_key)}&units=metric'
            try:
                resp = requests.get(url=geo_URL)
                result = resp.json()
            except Exception as e:
                print('Request error!')
                print(e)
                return 'Fail'
            print(f'Предлагаемое имя: {str(result[0].get('name'))}, страна: {str(result[0].get('country'))}, регион: {str(result[0].get('state'))}, lat: {str(result[0].get('lat'))}, lon: {str(result[0].get('lon'))}')
            req1 = str(input('Подтверждаете внесение (Y/N)? '))
            if req1 == 'Y' or req1 == 'y':
                city_list.append(str(result[0].get('name')))
                see_list(city_list)
            continue
        elif req == 'D' or req == 'd':
            req1 = input('Введите номер удаляемого города: ? ')
            try:
                ind = int(req1)
            except:
                print('Некорректное значение!')
                continue
            if ind >= len(city_list):
                print('Некорректный номер!')
                continue
            city_list.pop(ind)
            see_list(city_list)
            continue
    write_cities(city_list)


set_list()