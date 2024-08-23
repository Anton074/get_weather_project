import requests
from config.global_config import API_key, URL_curweather
class CurWeather():
    ___city: str

    def __init__(self, city_name):
        self.__city = city_name

    def get_current_weather(self):
        cur_URL = f'{str(URL_curweather)}?q={str(self.__city)}&appid={str(API_key)}&units=metric'
        try:
            resp = requests.get(url=cur_URL)
            result = resp.json()
        except Exception as e:
            print('Ошибка выполнения запроса!')
            print(e)
            return 'Fail'
        res_dict = {
            'main': result.get('weather')[0].get('main'),
            'temp': result.get('main').get('temp'),
            'temp_feel': result.get('main').get('feels_like'),
            'humidity': result.get('main').get('humidity'),
            'pressure': int(int(result.get('main').get('pressure'))*0.750064),
            'wind_speed': result.get('wind').get('speed'),
            'wind_direction': result.get('wind').get('deg'),
        }
        return res_dict

chel = CurWeather('Chelyabinsk')
res = chel.get_current_weather()
print('Chelyabinsk weather:')
print(res)
mos = CurWeather('Moscow')
res = mos.get_current_weather()
print('Moscow weather:')
print(res)