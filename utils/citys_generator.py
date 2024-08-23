import yaml, sys
sys.path.append("..")
# from config.global_config import API_key

city_list = ['Moscow', 'Chelyabinsk']
with open('../config/cities.yaml', 'w') as file:
    yaml.dump(city_list, file)