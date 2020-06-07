import requests
from requests.exceptions import HTTPError
from zipfile import ZipFile
from io import BytesIO

class AmplitudeClient:
    def __init__(self, api_key, secret_key):
        self.__api_key = api_key
        self.__secret_key = secret_key
    
    def export_data(self, start_date, end_date):
        api_url = 'https://amplitude.com/api/2/export'
        
        start_date = start_date.strftime('%Y%m%dT%H')
        end_date = end_date.strftime('%Y%m%dT%H')
        
        params = {
            'start': start_date,
            'end': end_date
        }
        
        with requests.get(url=api_url, auth=(api_key,secret_key),params=params, stream=True) as r:
            try:
                r.raise_for_status()
                data = ZipFile(BytesIO(r.content)).extractall()
                return data
            except HTTPError as e:
                print('error status', e)