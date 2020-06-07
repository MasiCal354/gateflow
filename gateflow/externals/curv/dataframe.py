import pandas as pd
import requests
from .client import CurvClient
import numpy as np


class CurvDataFrame:
    """
    Parser to read JSON response from CurvClient
    endpoint methods into pandas dataframe.
    """

    def __init__(self, host, jwt, organization_id,
                 requests_session=requests.Session()):
        self.__client = CurvClient(host, jwt, requests_session)
        self.__organization_id = organization_id

    def addresses(self):
        organization_id = self._get_organization_id()
        client = self._get_client()
        resp = client.list_all_saved_addresses(organization_id)
        if bool(resp['results']) == False:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame(resp['results'])
            df['currency'] = df['currency'].apply(lambda x: x['currency_id'])
            df = df.rename(columns={'currency': 'currency_id'})
            df['created'] = pd.to_datetime(df['created'], utc=True)
        return df

    def address_lists(self):
        organization_id = self._get_organization_id()
        client = self._get_client()
        resp = client.list_all_address_lists(organization_id)
        if bool(resp['results']) == False:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame(resp['results'])
            df['currency'] = df['currency'].apply(lambda x: x['currency_id'])
            df = df.rename(columns={'currency': 'currency_id'})
            df['created'] = pd.to_datetime(df['created'], utc=True)
            df['modified'] = pd.to_datetime(df['modified'], utc=True)
        return df

    def currencies(self):
        """
        problem with bip32_network_versions
        """
        organization_id = self._get_organization_id()
        client = self._get_client()
        resp = client.list_currencies(organization_id)
        if bool(resp['results']) == False:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame(resp['results'])
        return df

    def device_keys(self):
        organization_id = self._get_organization_id()
        client = self._get_client()
        resp = client.list_device_keys(organization_id)
        if bool(resp['results']) == False:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame(resp['results'])
            df['device_name'] = df['device'].apply(lambda x: x['name'])
            df['device_user'] = df['device'].apply(lambda x: x['user'])
            df['device_created'] = df['device'].apply(lambda x: x['created'])
            df['device_user_id'] = df['device_user'].apply(
                lambda x: x[list(x.keys())[0]])
            df['device_user_type'] = df['device_user'].apply(
                lambda x: list(x.keys())[0][:-3])
            df = df.drop(columns=['device', 'device_user'])
            df['device_created'] = pd.to_datetime(
                df['device_created'], utc=True)
        return df

    def keys(self):
        organization_id = self._get_organization_id()
        client = self._get_client()
        resp = client.list_keys(organization_id)
        if bool(resp['results']) == False:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame(resp['results'])
            df['created'] = pd.to_datetime(df['created'], utc=True)
        return df

    def service_accounts(self):
        organization_id = self._get_organization_id()
        """
        Still have a problem with api_keys
        """
        client = self._get_client()
        resp = client.list_service_accounts(organization_id)
        if bool(resp['results']) == False:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame(resp['results'])
            df['is_suspended'] = df['state'].apply(lambda x: x['is_suspended'])
            df['is_administrator'] = df['state'].apply(
                lambda x: x['is_administrator'])
            df['user_role'] = df['state'].apply(lambda x: x['user_role'])
            df['service_account_id'] = df['service_account_details'].apply(
                lambda x: x['service_account_id'])
            df['name'] = df['service_account_details'].apply(
                lambda x: x['name'])
            df['email'] = df['service_account_details'].apply(
                lambda x: x['email'])
            df['description'] = df['service_account_details'].apply(
                lambda x: x['description'])
            df['api_keys'] = df['service_account_details'].apply(
                lambda x: x['api_keys'])
            df = df.drop(columns=['state', 'service_account_details'])
        return df

    def transactions(self):
        organization_id = self._get_organization_id()
        """
        Still have a problem with user_activity, sources and destinations
        """
        client = self._get_client()
        resp = client.list_transactions(organization_id)
        if bool(resp['results']) == False:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame(resp['results'])
            df['block_number'] = df['block'].apply(
                lambda x: x['block_number'] if x is not None else np.NaN)
            df['block_hash'] = df['block'].apply(
                lambda x: x['block_hash'] if x is not None else np.NaN)
            df['previous_block_hash'] = df['block'].apply(
                lambda x: x['previous_block_hash'] if x is not None else np.NaN)
            df['state'] = df['block'].apply(
                lambda x: x['state'] if x is not None else np.NaN)
            df['confirmations'] = df['block'].apply(
                lambda x: x['confirmations'] if x is not None else np.NaN)
            df['currency'] = df['currency'].apply(lambda x: x['currency_id'])
            df = df.rename(columns={'currency': 'currency_id'})
            df['sources'] = df['details'].apply(
                lambda x: x['sources'] if 'sources' in x.keys() else np.NaN)
            df['destinations'] = df['details'].apply(
                lambda x: x['destinations'] if 'destinations' in x.keys() else np.NaN)
            df['type'] = df['details'].apply(
                lambda x: x['type'] if 'type' in x.keys() else np.NaN)
            df['fees_value_when_mined_in_us_cents'] = df['details'].apply(
                lambda x: x['fees_value_when_mined_in_us_cents'] if 'fees_value_when_mined_in_us_cents' in x.keys() else np.NaN)
            df['fees'] = df['details'].apply(
                lambda x: x['fees'] if 'fees' in x.keys() else np.NaN)
            df['gas_used'] = df['details'].apply(
                lambda x: x['gas_used'] if 'gas_used' in x.keys() else np.NaN)
            df['gas_price'] = df['details'].apply(
                lambda x: x['gas_price'] if 'gas_price' in x.keys() else np.NaN)
            df['gas_limit'] = df['details'].apply(
                lambda x: x['gas_limit'] if 'gas_limit' in x.keys() else np.NaN)
            df['fee_per_byte'] = df['details'].apply(
                lambda x: x['fee_per_byte'] if 'fee_per_byte' in x.keys() else np.NaN)
            df['max_length_in_bytes'] = df['details'].apply(
                lambda x: x['max_length_in_bytes'] if 'max_length_in_bytes' in x.keys() else np.NaN)
            df['mined_timestamp'] = df['timestamps'].apply(
                lambda x: x['mined_timestamp'])
            df['completed_timestamp'] = df['timestamps'].apply(
                lambda x: x['completed_timestamp'])
            df['mined_timestamp'] = pd.to_datetime(
                df['mined_timestamp'], utc=True)
            df['completed_timestamp'] = pd.to_datetime(
                df['completed_timestamp'], utc=True)
            df = df.drop(columns=['block', 'details', 'timestamps'])
            float_columns = [
                'fees',
                'gas_used',
                'gas_price',
                'gas_limit',
                'fee_per_byte',
                'max_length_in_bytes']
            df[float_columns] = df[float_columns].astype('float')
        return df

    def users(self):
        organization_id = self._get_organization_id()
        client = self._get_client()
        resp = client.list_users(organization_id)
        if bool(resp['results']) == False:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame(resp['results'])
            df = df[df['details'].apply(lambda x: x['type']) == 'regular_user']
            df = df.reset_index(drop=True)
            df['is_suspended'] = df['state'].apply(lambda x: x['is_suspended'])
            df['is_administrator'] = df['state'].apply(
                lambda x: x['is_administrator'])
            df['user_role'] = df['state'].apply(lambda x: x['user_role'])
            df['user_id'] = df['details'].apply(lambda x: x['user_id'])
            df['email'] = df['details'].apply(lambda x: x['email'])
            df['first_name'] = df['details'].apply(lambda x: x['first_name'])
            df['last_name'] = df['details'].apply(lambda x: x['last_name'])
            df['phone_number'] = df['details'].apply(
                lambda x: x['phone_number'])
            df['created'] = df['details'].apply(lambda x: x['created'])
            df['can_resend_invitation'] = df['details'].apply(
                lambda x: x['can_resend_invitation'])
            df['type'] = df['details'].apply(lambda x: x['type'])
            df = df.drop(columns=['state', 'details'])
            df['created'] = pd.to_datetime(df['created'])
        return df

    def wallets(self):
        organization_id = self._get_organization_id()
        client = self._get_client()
        resp = client.list_wallets(organization_id)
        if bool(resp['results']) == False:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame(resp['results'])
            df['currency'] = df['currency'].apply(lambda x: x['currency_id'])
            df = df.rename(columns={'currency': 'currency_id'})
            df['is_suspended'] = df['state'].apply(lambda x: x['is_suspended'])
            df['related_wallet'] = df['related_wallet'].apply(
                lambda x: x['wallet_id'] if x is not np.NaN else np.NaN)
            df = df.drop(columns=['state'])
            df['created'] = pd.to_datetime(df['created'], utc=True)
            df['modified'] = pd.to_datetime(df['modified'], utc=True)
        return df

    def wallet_groups(self):
        organization_id = self._get_organization_id()
        client = self._get_client()
        resp = client.list_wallet_groups(organization_id)
        if bool(resp['results']) == False:
            df = pd.DataFrame()
        else:
            df = pd.DataFrame(resp['results'])
            df['currency'] = df['currency'].apply(lambda x: x['currency_id'])
            df = df.rename(columns={'currency': 'currency_id'})
            df['created'] = pd.to_datetime(df['created'], utc=True)
            df['modified'] = pd.to_datetime(df['modified'], utc=True)
        return df

    def wallet_addresses(self):
        organization_id = self._get_organization_id()
        client = self._get_client()
        w = self.wallets()['wallet_id']
        frames = list()
        for wallet_id in w:
            resp = client.list_wallet_addresses(organization_id, wallet_id)
            if bool(resp['results']) == False:
                pass
            else:
                frame = pd.DataFrame(resp['results'])
                frame['wallet_id'] = wallet_id
                frame['created'] = pd.to_datetime(frame['created'], utc=True)
                frames.append(frame)
        df = pd.concat(frames)
        df = df.reset_index(drop=True)
        return df

    def _get_client(self):
        return self.__client

    def _get_organization_id(self):
        return self.__organization_id
