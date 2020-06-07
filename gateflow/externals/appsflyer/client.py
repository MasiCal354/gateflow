import requests
from requests.exceptions import HTTPError
from .auth import AppsFlyerAuth
import pandas as pd
from io import StringIO

class AppsFlyerClient:
    __API_VERSION = 'v5'
    def __init__(self, app_id, api_token, requests_session=requests.Session()):
        self.__base_url = 'https://hq.appsflyer.com/export/{}/'.format(app_id)
        self.__api_token = api_token
        self.__requests_session = requests_session
    
    def _handle_response(self):
        response = self._get_response()
        response.raise_for_status()
        return pd.read_csv(StringIO(response.text))
            
    def _request(self, method, report_type, params=None):
        url = self._get_base_url() + report_type + '/' + self.__API_VERSION
        api_token = self._get_api_token()
        requests_session = self._get_requests_session()
        # auth = AppsFlyerAuth(api_token)

        # response = getattr(requests_session, method)(url, auth=auth, params=params)
        params['api_token'] = api_token
        response = getattr(requests_session, method)(url, params=params)
        self._set_response(response)
        return self._handle_response()
    
    def _get(self, report_type, params=None):
        return self._request('get', report_type, params=params)
    
    def partners_report(self, params):
        report_type = 'partners_report'
        return self._get(report_type, params)
        
    def partners_by_date_report(self, params):
        report_type = 'partners_by_date_report'
        return self._get(report_type, params)
        
    def daily_report(self, params):
        report_type = 'daily_report'
        return self._get(report_type, params)
        
    def geo_report(self, params):
        report_type = 'geo_report'
        return self._get(report_type, params)
        
    def geo_by_date_report(self, params):
        report_type = 'geo_by_date_report'
        return self._get(report_type, params)
        
    def installs_report(self, params):
        report_type = 'installs_report'
        return self._get(report_type, params)
    '''
    def in_app_events_report(self, params):
        report_type = 'in_app_events_report'
        return self._get(report_type, params)
    ''' 
    def uninstall_events_report(self, params):
        report_type = 'uninstall_events_report'
        return self._get(report_type, params)
        
    def organic_installs_report(self, params):
        report_type = 'organic_installs_report'
        return self._get(report_type, params)
    '''
    def organic_in_app_events_report(self, params):
        report_type = 'organic_in_app_events_report'
        return self._get(report_type, params)
        
    def ad_revenue_raw(self, params):
        report_type = 'ad_revenue_raw'
        return self._get(report_type, params)
        
    def ad_revenue_organic_raw(self, params):
        report_type = 'ad_revenue_organic_raw'
        return self._get(report_type, params)
    '''
    def _get_base_url(self):
        return self.__base_url

    def _get_api_token(self):
        return self.__api_token

    def _get_requests_session(self):
        return self.__requests_session

    def _get_response(self):
        return self.__response

    def _set_response(self, response):
        self.__response = response

        