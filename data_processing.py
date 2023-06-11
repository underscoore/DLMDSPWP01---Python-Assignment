import pandas
import numpy as np


class DataProcessing:
    '''Finding Sum of least squires'''
    def find_sum_of_least_squares(self, x, y):
        x = np.array(x)
        y = np.array(y)
        difference = np.subtract(x, y)
        square = np.square(difference)
        sumOfSquares = np.sum(square)
        return sumOfSquares


    '''finding Least Squires'''
    def find_least_squares(self, x, y):
        x = np.array(x)
        y = np.array(y)
        difference = np.subtract(x, y)
        square = np.square(difference)
        return pandas.DataFrame(square)

    '''Finding deviations'''
    def find_deviation(self, x, y):
        x = np.array(x)
        y = np.array(y)
        difference = np.subtract(x, y)
        return pandas.DataFrame(difference)

    '''Findind any deviation greater than threshold'''
    def any_deviation_greater_than_threshold(self, x, y, threshold):
        x = np.array(x)
        y = np.array(y)
        difference = pandas.DataFrame(np.subtract(x, y))
        return (difference > threshold).any().any()