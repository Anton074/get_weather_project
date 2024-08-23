import pandas as pd

class csv_operataions():
    __fn: str

    def __init__(self, filename):
        self.__fn = filename

    def write_to_file(self, data):
        df1 = pd.DataFrame(data)
        try:
            df1.to_csv(self.__fn, index=False)
            return('Success')
        except Exception as e:
            print('Failed to write CSV')
            print(e)
            return 'Fail'

    def get_data(self):
        try:
            df1 = pd.read_csv(self.__fn)
            return df1
        except Exception as e:
            print('Failed to load!')
            print(e)
            return 'Fail'