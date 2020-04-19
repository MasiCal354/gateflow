class Writer:
    def __init__(self):
        pass
    
    def from_frame(self, source, target, if_exists):
        pass
    
    def from_frames(self, sources, targets, if_exists):
        pass
    
class GBQWriter(Writer):
    def __init__(self, project_id, service_account_path):
        self.__credentials = service_account.Credentials.from_service_account_file(service_account_key)
        self.__project_id = project_id
        
    def from_frame(self, source, target, if_exists):
        pass
        
    def get_credentials(self):
        return self.__credentials
    def get_project_id(self):
        return self.__project_id
    def set_credentials(self, credentials):
        self.__credentials = crendentials
    def set_project_id(self, project_id):
        self.__project_id = project_id