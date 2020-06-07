from .client import IndodaxClient
import requests
import pandas as pd
import numpy as np


class IndodaxDataFrame:
    def __init__(self, key, secret, pairs,
                 requests_session=requests.Session()):
        self.__client = IndodaxClient(key, secret, requests_session)
        self.__pairs = pairs

    def user_balances(self):
        client = self._get_client()
        resp = client.get_info()
        resp = resp['return']
        l = list()
        for k in resp['balance'].keys():
            l.append({
                'user_id': resp['user_id'],
                'name': resp['name'],
                'email': resp['email'],
                'profile_picture': resp['profile_picture'],
                'verification_status': resp['verification_status'],
                'gauth_enable': resp['gauth_enable'],
                'currency': k,
                'balance': resp['balance'][k],
                'balance_hold': resp['balance_hold'][k] if k in resp['balance_hold'].keys() else np.NaN,
                'address': resp['address'][k] if k in resp['address'].keys() else np.NaN,
                'server_time': resp['server_time']
            })
        df = pd.DataFrame(l)
        df['user_id'] = df['user_id'].astype(int)
        df[['balance', 'balance_hold']] = df[[
            'balance', 'balance_hold']].astype(float)
        df['server_time'] = pd.to_datetime(df['server_time'] * 10**9, utc=True)
        return df

    def trades(self):
        pairs = self._get_pairs()
        client = self._get_client()
        frames = list()
        for pair in pairs:
            currency = pair.split('_')[0]
            paired_currency = pair.split('_')[1]

            resp = client.trade_history(pair)
            frame = pd.DataFrame(resp['return']['trades'])

            frame = frame.rename(columns={currency: 'amount'})

            frame['currency'] = currency
            frame['paired_currency'] = paired_currency

            frame[['trade_id', 'order_id', 'trade_time']] = frame[[
                'trade_id', 'order_id', 'trade_time']].astype(int)
            frame[['amount', 'price', 'fee']] = frame[[
                'amount', 'price', 'fee']].astype(float)
            frame['trade_time'] = pd.to_datetime(
                frame['trade_time'].astype(int) * 10**9, utc=True)

            frames.append(frame)

        df = pd.concat(frames).sort_values('trade_id').reset_index(drop=True)
        return df

    def orders(self):
        pairs = self._get_pairs()
        client = self._get_client()
        frames = list()
        for pair in pairs:
            currency = pair.split('_')[0]
            paired_currency = pair.split('_')[1]

            resp = client.order_history(pair)
            frame = pd.DataFrame(resp['return']['orders'])

            frame = frame.rename(columns={
                'order_' + currency: 'ordered_amount',
                'remain_' + currency: 'remaining_amount',
                'order_' + paired_currency: 'ordered_paired_amount',
                'remain_' + paired_currency: 'remaining_paired_amount'
            })

            frame['currency'] = currency
            frame['paired_currency'] = paired_currency

            frame[['order_id', 'submit_time', 'finish_time']] = frame[[
                'order_id', 'submit_time', 'finish_time']].astype(int)
            float_columns = [
                'ordered_amount',
                'remaining_amount',
                'ordered_paired_amount',
                'remaining_paired_amount']
            frame[float_columns] = frame[float_columns].astype(float)
            frame['submit_time'] = pd.to_datetime(
                frame['submit_time'] * 10**9, utc=True)
            frame['finish_time'] = pd.to_datetime(
                frame['finish_time'] * 10**9, utc=True)

            frames.append(frame)

        df = pd.concat(frames).sort_values('order_id').reset_index(drop=True)
        return df

    def _get_client(self):
        return self.__client

    def _get_pairs(self):
        return self.__pairs
