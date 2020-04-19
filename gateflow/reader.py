import pandas as pd
import pandas_gbq as pbq
from sqlalchemy import create_engine, MetaData
from google.oauth2 import service_account
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from pymongo import MongoClient
from externals.curv import CurvDataFrame

class Reader:
    """
    Parent Class for all reader in this module.
    The structure of this class is to make all
    child class can read table, multiple tables
    and all tables inside the database and
    return it as a dataframe or dictionary
    of dataframe with table name as the key.
    """
    def __init__(self):
        pass
    
    def read_table(self, table_name):
        pass
    
    def read_tables(self, table_names):
        frames = dict()
        for table_name in table_names:
            df = self.read_table(table_name)
            frames.update({table_name:df})
        return frames

    def list_tables(self):
        pass
    
    def read_all_tables(self):
        table_names = self.list_tables()
        frames = self.read_tables(table_names)
        return frames

class SQLReader(Reader):
    def __init__(self, db_uri):
        self.__engine = create_engine(db_uri)
    
    def read_table(self, table_name):
        engine = self.get_engine()
        conn = engine.connect()
        df = pd.read_sql_table(table_name, conn)
        return df
    
    def list_tables(self):
        metadata = MetaData()
        engine = self.get_engine()
        metadata.reflect(engine)
        tables = list(metadata.tables.keys())
        return tables
    
    def get_engine(self):
        return self.__engine

    def set_engine(self, engine):
        self.__engine = engine
        
class MongoReader(Reader):
    def __init__(self, db_uri, db_name):
        self.__db = MongoClient(db_uri)[db_name]
    
    def read_table(self, table_name):
        db = self.get_db()
        df = pd.DataFrame(list(db[table_name].find()))
        return df
    
    def list_tables(self):
        db = self.get_db()
        tables = list(db.list_collection_names())
        return tables
    
    def get_db(self):
        return self.__db
    
    def set_db(self, db):
        self.__db = db
        
class GoogleSheetReader(Reader):
    def __init__(self, service_account_path, file_key):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(service_account_path, scope)
        gc = gspread.authorize(credentials)
        self.__sh = gc.open_by_key(file_key)
    
    def read_table(self, table_name):
        sh = self.get_sh()
        worksheet = sh.worksheet(table_name)
        data = worksheet.get_all_values()
        headers = data.pop(0)
        df = pd.DataFrame(data, columns=headers)
        return df
    
    def list_tables(self):
        sh = self.get_sh()
        tables = sh.worksheets()
        return tables
    
    def get_sh(self):
        return self.__sh
    
    def set_sh(self, sh):
        self.__sh = sh

class GBQReader(Reader):
    def __init__(self, project_id, service_account_path, dataset):
        self.__project_id = project_id
        self.__credentials = service_account.Credentials.from_service_account_file(service_account_path)
        self.__dataset = dataset
    
    def read_table(self, table_name):
        project_id = self.get_project_id()
        credentials = self.get_credentials()
        dataset = self.get_dataset()
        query = 'SELECT * FROM {}.{}'.format(dataset, table_name)
        df = pbq.read_gbq(query, project_id, credentials = credentials)
        return df
    
    def list_tables(self):
        df = self.read_table('INFORMATION_SCHEMA.TABLES')
        tables = list(df['table_name'])
        return tables
    
    def get_project_id(self):
        return self.__project_id
    
    def set_project_id(self, project_id):
        self.__project_id = project_id
    
    def get_credentials(self):
        return self.__credentials
    
    def set_credentials(self, credentials):
        self.__credentials = credentials
    
    def get_dataset(self):
        return self.__dataset
    
    def set_dataset(self, dataset):
        self.__dataset = dataset
        
class CurvReader(Reader):
    def __init__(self, host, jwt, organization_id = ''):
        self.__gt = CurvDataFrame(host, jwt, organization_id)
    
    def read_table(self, table_name):
        gt = self.get_gt()
        df = getattr(gt, table_name)()
        return df
    
    def list_tables(self):
        gt = self.get_gt()
        tables = [method for method in dir(gt) if method[:2] != '__' and method[1:4] != 'et_']
        return tables
    
    def get_project_id(self):
        return self.__project_id
    
    def set_project_id(self, project_id):
        self.__project_id = project_id
    
    def get_credentials(self):
        return self.__credentials
    
    def set_credentials(self, credentials):
        self.__credentials = credentials
    
    def get_dataset(self):
        return self.__dataset
    
    def set_dataset(self, dataset):
        self.__dataset = dataset
        
class IndodaxReader():
    
class BinanceReader():