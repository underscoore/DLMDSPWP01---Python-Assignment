import pandas
from data_processing import DataProcessing

class Ideal(DataProcessing):
    def load_ideal_data(self):
        self.ideal = pandas.read_csv("dataset/ideal.csv")
        return self.ideal

    def find_ideal(self, x):
        database = DataProcessing()
        least_squares = [database.find_sum_of_least_squares(x, self.ideal.iloc[:, i]) for i in
                         range(len(self.ideal.columns))]
        print(least_squares)

        first_four_least_squares = sorted(least_squares)[:4]
        indices = [least_squares.index(i) for i in first_four_least_squares]
        ideal_functions = [self.ideal.iloc[:, i] for i in indices]

        ideal_functions = pandas.DataFrame(ideal_functions).transpose()
        ideal_functions.columns = ['y1', 'y2', 'y3', 'y4']
        return ideal_functions