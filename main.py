import sys
sys.path.append("..")

from utils.cities_reader import Cities
import utils.weather, utils.write_to_csv

def get_current_weather():
    """This function requests current weather in towns from file config/cities.yaml,
    places result in file result.csv,
    returns Success if everything is ok, Fail is something wrong and error type
    """
    cities_list = Cities.get_cities_list('config/cities.yaml')
    if cities_list == 'Fail':
        return 'Fail'
    weather_list = []
    for A in cities_list:
        town = utils.weather.CurWeather(A)
        t = town.get_current_weather()
        if t == 'Fail':
            return 'Fail'
        weather_list.append(t)
    my_csv = utils.write_to_csv.csv_operataions('result.csv')
    flag = my_csv.write_to_file(weather_list)
    if flag == 'Fail':
        return 'Fail'
    return 'Success'

flag = get_current_weather()
if flag:
    print('Success')
else:
    print('Fail')