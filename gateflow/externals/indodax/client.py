import requests
from .auth import IndodaxAuth
from .utils import *


class IndodaxClient:
    API_URL = 'https://indodax.com/tapi'

    def __init__(self, key, secret, requests_session=requests.Session()):
        self.__key = key
        self.__secret = secret
        self.__request_session = requests_session

    def __post(self, method, params):
        url = self.API_URL
        key = self.get_key()
        secret = self.get_secret()
        request_session = self.get_request_session()

        params['method'] = method
        params['nonce'] = nonce()
        sign = signature(secret, params)

        auth = IndodaxAuth(key, sign)
        response = request_session.post(url, data=params, auth=auth)
        response = response.json()
        return response

    def get_info(self):
        return self.__post('getInfo', {})

    def trans_history(self):
        return self.__post('transHistory', {})

    def trade(self, pair, ttype, amount, price):
        currency = pair.split('_')[0]
        paired_currency = pair.split('_')[0]
        params = {
            'pair': pair,
            'type': ttype,
            'price': price}
        if ttype == 'buy':
            params[paired_currency] = amount
        elif ttype == 'sell':
            params[currency] = amount
        return self.__post('trade', params)

    def trade_history(self, pair, **kwargs):
        '''Keyword arguments : count, from_id, end_id, order, since, end'''
        params = {
            'pair': pair
        }
        if kwargs:
            for key, value in kwargs.items():
                params[key] = value
        return self.__post('tradeHistory', params)

    def open_orders(self, pair):
        params = {'pair': pair}
        return self.__post('openOrders', params)

    def order_history(self, pair, **kwargs):
        '''Keyword arguments : count, from'''
        params = {
            'pair': pair
        }
        if kwargs:
            for key, value in kwargs.items():
                params[key] = value
        return self.__post('orderHistory', params)

    def get_order(self, pair, order_id):
        params = {
            'pair': pair,
            'order_id': order_id
        }
        return self.__post('getOrder', params)

    def cancel_order(self, pair, ttype, order_id):
        params = {
            'pair': pair,
            'order_id': order_id,
            'type': ttype
        }
        return self.__post('cancelOrder', params)

    def get_key(self):
        return self.__key

    def get_secret(self):
        return self.__secret

    def get_request_session(self):
        return self.__request_session
