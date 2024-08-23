import yaml

class Cities():
    def __init__(self):
        pass

    @staticmethod
    def get_cities_list(filename: str):
        try:
            with open(filename) as file:
                docs = yaml.load(file, Loader=yaml.FullLoader)
                return docs
        except Exception as e:
            print('Cities names read error!')
            print(e)
            return 'Fail'