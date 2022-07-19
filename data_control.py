import pandas as pd


class Data:
    def __init__(self, source):
        self.source = source

    def data_base(self):
        data_base_object = pd.read_csv(self.source)
        return data_base_object, len(data_base_object)

