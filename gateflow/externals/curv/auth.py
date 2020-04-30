from requests.auth import AuthBase


class CurvAuth(AuthBase):
    """
    Authentication class for Curv API
    """

    def __init__(self, json_web_token):
        self.__jwt = json_web_token

    def __call__(self, r):
        jwt = self.get_jwt()
        r.headers['Authorization'] = 'Bearer ' + jwt
        return r

    def get_jwt(self):
        return self.__jwt

    def set_jwt(self, jwt):
        self.__jwt = jwt
