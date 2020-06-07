import os
import pandas as pd
from sqlalchemy import create_engine, inspect
from datetime import datetime
import subprocess

class Scheduler:
    def __init__(self, db_uri):
        self.__engine = create_engine(db_uri)
        ins = inspect(sekf.__engine)
        if 'gateflow_schedule' in ins.get_table_names():
            self.__df = pd.read_sql('gateflow_schedule', self.__engine)
        else:
            self.__df = pd.DataFrame(
                columns=[
                    'schedule_id',
                    'crontab_path',
                    'cron_expression',
                    'python_path',
                    'file_path',
                    'log_path',
                    'created_at',
                    'updated_at'])

    def add_schedule(self, crontab_path, cron_expression,
                     python_path, file_path, log_path='/dev/null'):
        df = self.get_df()
        data = [{
            'schedule_id': 1 if df.empty else df['schedule_id'].max() + 1,
            'crontab_path': crontab_path,
            'cron_expression': cron_expression,
            'python_path': python_path,
            'file_path': file_path,
            'log_path': log_path,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }]
        df = pd.concat([df, pd.DataFrame(data)])

        self.set_df(df)

    def update_schedule(self, schedule_id, **kwargs):
        df = self.get_df()
        for k in kwargs.keys():
            df[df['schedule_id'] == schedule_id][k] = kwargs[k]
        df[df['schedule_id'] == schedule_id]['updated_at'] = datetime.now()

        self.set_df(df)

    def delete_schedule(self, schedule_id):
        df = self.get_df()
        df = df[df['schedule_id'] != schedule_id]

        self.set_df(df)

    def update_database(self):
        df = self.get_df()
        engine = self.get_engine()
        df.to_sql('gateflow_schedule', engine, if_exists='replace')

    def write_crontab(self):
        df = self.get_df()
        df['row'] = df['cron_expression'] + ' ' + df['python_path'] + \
            ' ' + df['file_path'] + ' >>' + df['log_path'] + '2>&1'
        texts = dict()
        for cron_path in df['cron_path']:
            text = ''
            for row in df['row']:
                text += row + '\n'

            if cron_path in texts.keys():
                texts[cron_path] += text
            else:
                texts.update({cron_path: text})

        command = 'cat '
        for cron_path in texts.keys():
            command += cron_path + ' '
            with open(cron_path, 'w') as f:
                f.write(texts[cron_path])
        command += '| crontab'

        subprocess.call(command, shell=True)

    def get_df(self):
        return self.__df

    def get_engine(self):
        return self.__engine

    def set_df(self, df):
        self.__df = df
