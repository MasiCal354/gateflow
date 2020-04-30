import pandas as pd
import pandas_gbq as pbq
from google.oauth2 import service_account


class GBQWriter:
    def __init__(self, project_id, service_account_path):
        self.__credentials = service_account.Credentials.from_service_account_file(
            service_account_path)
        self.__project_id = project_id

    def from_frame(self, source, target, if_exists):
        credentials = self.get_credentials()
        project_id = self.get_project_id()
        source.to_gbq(target, project_id, if_exists=if_exists,
                      credentials=credentials, progress_bar=False)

    def from_frames(self, sources, target_dataset, if_exists):
        for k in sources.keys():
            self.from_frame(sources[k], target_dataset +
                            '.' + k, if_exists=if_exists)

    def get_credentials(self):
        return self.__credentials

    def get_project_id(self):
        return self.__project_id

    def set_credentials(self, credentials):
        self.__credentials = crendentials

    def set_project_id(self, project_id):
        self.__project_id = project_id
