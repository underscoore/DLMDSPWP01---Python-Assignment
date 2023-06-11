import sqlite3
from bokeh.plotting import figure, show
import pandas as pd
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource
import matplotlib.pyplot as plt

class DataVisualization:

    def plot_train_data_scatter():
        conn = sqlite3.connect('DataBase.db')
        query = 'SELECT * FROM train_data'   
        # Query the data from the "ideal_data" table

        df = pd.read_sql_query(query, conn)
        x = df['x']
        y1 = df['y1']
        y2 = df['y2']
        y3 = df['y3']
        y4 = df['y4']

        #configuring the Graph properties
        plt.title('\n "X" against Y1, Y2, Y3, Y4 from trained data \n', fontdict={'fontsize':20, 'fontweight': 5, 'color': 'Black'})
        plt.xlabel("X values", fontdict={'fontsize': 10, 'fontweight': 10, 'color': 'blue'})
        plt.ylabel("Y Values", fontdict={'fontsize': 10, 'fontweight': 10, 'color': 'blue'})

        # Ploting the graph
        plt.scatter(x, y1, alpha=1, s=5, c='blue', label = 'X vs Y1')
        plt.scatter(x, y2, alpha=1, s=5, c='red', label = 'X vs Y2')
        plt.scatter(x, y3, alpha=1, s=5, c='green', label = 'X vs Y3')
        plt.scatter(x, y4, alpha=1, s=5, c='yellow', label = 'X vs Y4')

        # adding legends
        plt.legend()

        # Calling the function to show the plot
        plt.show()

        # Close the database connection
        conn.close()

