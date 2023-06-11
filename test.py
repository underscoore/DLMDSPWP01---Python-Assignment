import pandas
from data_processing import DataProcessing

class Test(DataProcessing):
    def load_test_data(self):
        self.test = pandas.read_csv("dataset/test.csv")
        return self.test