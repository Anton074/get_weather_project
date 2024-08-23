import requests, datetime
from config.global_config import API_key, URL_curweather
class CurWeather():
    __city: str

    def __init__(self, city_name):
        self.__city = city_name

    def get_current_weather(self):
        """This function requests weather in current city for now and returns as dictionary"""
        cur_URL = f'{str(URL_curweather)}?q={str(self.__city)}&appid={str(API_key)}&units=metric'
        try:
            resp = requests.get(url=cur_URL)
            result = resp.json()
        except Exception as e:
            print('Request error!')
            print(e)
            return 'Fail'
        res_dict = {
            'date': datetime.date.today(),
            'town': self.__city,
            'main': result.get('weather')[0].get('main'),
            'temp': result.get('main').get('temp'),
            'temp_feel': result.get('main').get('feels_like'),
            'humidity': result.get('main').get('humidity'),
            'pressure': int(int(result.get('main').get('pressure'))*0.750064),
            'wind_speed': result.get('wind').get('speed'),
            'wind_direction': result.get('wind').get('deg'),
        }
        return res_dict