from requests.auth import AuthBase

class AppsFlyerAuth(AuthBase):
    def __init__(self, api_token):
        self.__api_token = api_token
    
    def __call__(self, r):
        r.prepare_url(r.url,{'api_token':self.get_api_token()})
        return r
        
    def get_api_token(self):
        return self.__api_token
    