from requests.auth import AuthBase


class IndodaxAuth(AuthBase):
    def __init__(self, key, sign):
        self.__key = key
        self.__sign = sign

    def __call__(self, request):
        key = self.get_key()
        sign = self.get_sign()

        request.headers['Key'] = key
        request.headers['Sign'] = sign

        return request

    def get_key(self):
        return self.__key

    def get_sign(self):
        return self.__sign
