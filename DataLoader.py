from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base


class DataLoader:

    '''Initializing the variables'''
    def __init__(self, dataBase, tableName, dataFrame):
        self.Base = declarative_base()
        self.dataBase = dataBase
        self.tableName = tableName
        self.dataFrame = dataFrame
        self.engine = create_engine('sqlite:///{}.db'.format(self.dataBase))    


    '''Loading data to data base'''
    def load_data(self):    
        self.Base.metadata.create_all(self.engine)
        table_name = self.tableName
        self.dataFrame.to_sql(table_name, con=self.engine, if_exists='replace', index=False)  


    '''Closing connection'''
    def close_connection(self):
        self.engine.dispose()


