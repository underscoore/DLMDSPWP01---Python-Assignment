import pandas
from data_processing import DataProcessing


class Train(DataProcessing):
    def load_training_data(self):
        self.train = pandas.read_csv("dataset/train.csv")
        return self.train

    def get_deviation(self, x):
        self.deviation = self.find_deviation(x, self.train.iloc[:, 1])
        return self.deviation