import requests
from requests.exceptions import HTTPError
from exceptions import CurvRequestException
from auth import CurvAuth

class CurvClient:
    API_VERSION = 'v1.0'
    def __init__(self, host, jwt, requests_session = requests.Session()):
        self.__base_url = host + '/api/policy/{}/'.format(self.API_VERSION)
        self.__jwt = jwt
        self.__requests_session = requests_session
    
    def _handle_response(self):
        """Internal helper for handling API responses from the Curv server.
        Raises the appropriate exceptions when necessary; otherwise, returns the
        response.
        """
        try:
            response = self._get_response()
            response.raise_for_status()
            return response.json()
        except ValueError:
            raise CurvRequestException('Invalid Response: %s' % response.text)
            
    def _request(self, method, path, params = None):
        url = self._get_base_url() + path
        jwt = self._get_jwt()
        requests_session = self._get_requests_session()
        auth = CurvAuth(jwt)
        
        method_arg = {
            'get': 'params',
            'post': 'data',
            'delete': 'data'
        }
        
        kwargs = {method_arg[method]: params}
        
        response = getattr(requests_session, method)(url, auth=auth, **kwargs)
        self._set_response(response)
        return self._handle_response()
    
    def _get(self, path, params=None):
        return self._request('get', path)
        
    def _post(self, path, params=None):
        return self._request('post', path, params)
    
    def _delete(self, path, params=None):
        return self._request('delete', path)
    
    # Curv Endpoint
    
    def list_all_saved_addresses(self, organization_id, params=None):
        path = 'organization/{}/address_book/address_book_entry/'
        path = path.format(organization_id)
        return self._get(path, params)

    def save_new_address(self, organization_id, params=None):
        path = 'organization/{}/address_book/address_book_entry/create_new/'
        path = path.format(organization_id)
        return self._post(path, params)

    def get_saved_address(self, organization_id, address_book_entry_id, params=None):
        path = 'organization/{}/address_book/address_book_entry/{}/'
        path = path.format(organization_id, address_book_entry_id)
        return self._get(path, params)

    def list_all_address_lists(self, organization_id, params=None):
        path = 'organization/{}/address_book/address_book_list/'
        path = path.format(organization_id)
        return self._get(path, params)

    def create_new_address_list(self, organization_id, params=None):
        path = 'organization/{}/address_book/address_book_list/create_new/'
        path = path.format(organization_id)
        return self._post(path, params)

    def get_address_list(self, organization_id, address_book_list_id, params=None):
        path = 'organization/{}/address_book/address_book_list/{}/'
        path = path.format(organization_id, address_book_list_id)
        return self._get(path, params)

    def list_address_list_entries(self, organization_id, address_book_list_id, params=None):
        path = 'organization/{}/address_book/address_book_list/{}/members/'
        path = path.format(organization_id, address_book_list_id)
        return self._get(path, params)

    def add_address_to_list(self, organization_id, address_book_list_id, params=None):
        path = 'organization/{}/address_book/address_book_list/{}/members/create_new/'
        path = path.format(organization_id, address_book_list_id)
        return self._post(path, params)

    def remove_address_from_list(self, organization_id, address_book_list_id, address_book_entry_id, params=None):
        path = 'organization/{}/address_book/address_book_list/{}/members/{}/'
        path = path.format(organization_id, address_book_list_id, address_book_entry_id)
        return self._delete(path, params)

    def get_usd_based_exchange_rates(self, params=None):
        path = 'exchange_rates/get_predefined_exchange_rates_usd_based=None/'
        path = path.format()
        return self._get(path, params)

    def list_currencies(self, organization_id, params=None):
        path = 'organization/{}/currency/'
        path = path.format(organization_id)
        return self._get(path, params)

    def get_currency_information(self, organization_id, currency_id, params=None):
        path = 'organization/{}/currency/{}/'
        path = path.format(organization_id, currency_id)
        return self._get(path, params)

    def get_suggested_transaction_fees(self, organization_id, currency_id, params=None):
        path = 'organization/{}/currency/{}/transaction_fees/'
        path = path.format(organization_id, currency_id)
        return self._get(path, params)

    def list_device_keys(self, organization_id, params=None):
        path = 'organization/{}/secure_operations/device/'
        path = path.format(organization_id)
        return self._get(path, params)

    def get_device_key(self, organization_id, device_key_id, params=None):
        path = 'organization/{}/secure_operations/device/{}/'
        path = path.format(organization_id, device_key_id)
        return self._get(path, params)

    def list_keys(self, organization_id, params=None):
        path = 'organization/{}/secure_operations/keys/'
        path = path.format(organization_id)
        return self._get(path, params)

    def get_key(self, organization_id, key_id, params=None):
        path = 'organization/{}/secure_operations/keys/{}/'
        path = path.format(organization_id, key_id)
        return self._get(path, params)

    def generate_key(self, organization_id, params=None):
        path = 'organization/{}/secure_operations/key_generation/'
        path = path.format(organization_id)
        return self._post(path, params)

    def load_key(self, organization_id, params=None):
        path = 'organization/{}/secure_operations/load_key/'
        path = path.format(organization_id)
        return self._post(path, params)

    def list_user_organizations(self, params=None):
        path = 'organization/list_user_organizations/'
        path = path.format()
        return self._get(path, params)

    def get_organization_information(self, organization_id, params=None):
        path = 'organization/{}/'
        path = path.format(organization_id)
        return self._get(path, params)

    def set_backup_public_key(self, organization_id, params=None):
        path = 'organization/{}/set_backup_public_key/'
        path = path.format(organization_id)
        return self._post(path, params)

    def get_recovery_info(self, organization_id, params=None):
        path = 'organization/{}/secure_operations/key_recovery/get_recovery_info/'
        path = path.format(organization_id)
        return self._get(path, params)

    def refresh_share(self, organization_id, params=None):
        path = 'organization/{}/secure_operations/refresh/'
        path = path.format(organization_id)
        return self._post(path, params)

    def send_share(self, organization_id, params=None):
        path = 'organization/{}/secure_operations/send_share/'
        path = path.format(organization_id)
        return self._post(path, params)

    def receive_shares(self, organization_id, params=None):
        path = 'organization/{}/secure_operations/receive_shares/'
        path = path.format(organization_id)
        return self._post(path, params)

    def provision_device(self, organization_id, params=None):
        path = 'organization/{}/secure_operations/provision_device/'
        path = path.format(organization_id)
        return self._post(path, params)

    def has_key_share(self, organization_id, params=None):
        path = 'organization/{}/secure_operations/has_key_share/'
        path = path.format(organization_id)
        return self._post(path, params)

    def self_managed_generate_key(self, organization_id, params=None):
        path = 'organization/{}/self_managed_secure_operations/key_generation/'
        path = path.format(organization_id)
        return self._post(path, params)

    def self_managed_sign_transaction(self, organization_id, params=None):
        path = 'organization/{}/self_managed_secure_operations/sign_transaction/'
        path = path.format(organization_id)
        return self._post(path, params)

    def self_managed_sign_and_schedule_transaction(self, organization_id, params=None):
        path = 'organization/{}/self_managed_secure_operations/sign_and_push/'
        path = path.format(organization_id)
        return self._post(path, params)

    def self_managed_load_provisioning_package(self, organization_id, params=None):
        path = 'organization/{}/self_managed_secure_operations/load_provisioning_package/'
        path = path.format(organization_id)
        return self._post(path, params)

    def self_managed_refresh_share(self, organization_id, params=None):
        path = 'organization/{}/self_managed_secure_operations/refresh/'
        path = path.format(organization_id)
        return self._post(path, params)

    def self_managed_retrieve_transaction(self, organization_id, params=None):
        path = 'organization/{}/self_managed_secure_operations/retrieve_and_parse_transaction/'
        path = path.format(organization_id)
        return self._post(path, params)

    def self_managed_send_share(self, organization_id, params=None):
        path = 'organization/{}/self_managed_secure_operations/send_share/'
        path = path.format(organization_id)
        return self._post(path, params)

    def self_managed_receive_shares(self, organization_id, params=None):
        path = 'organization/{}/self_managed_secure_operations/receive_shares/'
        path = path.format(organization_id)
        return self._post(path, params)

    def list_service_accounts(self, organization_id, params=None):
        path = 'organization/{}/service_account/'
        path = path.format(organization_id)
        return self._get(path, params)

    def get_service_account(self, organization_id, service_account_id, params=None):
        path = 'organization/{}/service_account/{}/'
        path = path.format(organization_id, service_account_id)
        return self._get(path, params)

    def list_transactions(self, organization_id, params=None):
        path = 'organization/{}/all_transactions/'
        path = path.format(organization_id)
        return self._get(path, params)

    def get_transaction(self, organization_id, transaction_id, params=None):
        path = 'organization/{}/all_transactions/{}/'
        path = path.format(organization_id, transaction_id)
        return self._get(path, params)

    def list_outgoing_transactions(self, organization_id, params=None):
        path = 'organization/{}/transaction/'
        path = path.format(organization_id)
        return self._get(path, params)

    def create_transaction(self, organization_id, params=None):
        path = 'organization/{}/transaction/create_new/'
        path = path.format(organization_id)
        return self._post(path, params)

    def get_outgoing_transaction(self, organization_id, transaction_id, params=None):
        path = 'organization/{}/transaction/{}/'
        path = path.format(organization_id, transaction_id)
        return self._get(path, params)

    def abort_transaction(self, organization_id, transaction_id, params=None):
        path = 'organization/{}/transaction/{}/abort/'
        path = path.format(organization_id, transaction_id)
        return self._delete(path, params)

    def schedule_transaction(self, organization_id, transaction_id, params=None):
        path = 'organization/{}/transaction/{}/push_to_chain/'
        path = path.format(organization_id, transaction_id)
        return self._post(path, params)

    def vote_on_transaction(self, organization_id, transaction_id, params=None):
        path = 'organization/{}/transaction/{}/vote/'
        path = path.format(organization_id, transaction_id)
        return self._post(path, params)

    def retrieve_transaction_voting_status(self, organization_id, transaction_id, params=None):
        path = 'organization/{}/transaction/{}/voting_status/'
        path = path.format(organization_id, transaction_id)
        return self._get(path, params)

    def sign_transaction(self, organization_id, params=None):
        path = 'organization/{}/secure_operations/sign_transaction/'
        path = path.format(organization_id)
        return self._post(path, params)

    def create_and_sign_blackbox_transaction(self, organization_id, params=None):
        path = 'organization/{}/secure_operations/create_and_sign_blackbox/'
        path = path.format(organization_id)
        return self._post(path, params)

    def retrieve_transaction_for_signing(self, organization_id, params=None):
        path = 'organization/{}/secure_operations/retrieve_transaction/'
        path = path.format(organization_id)
        return self._post(path, params)

    def mark_transaction_as_valid(self, organization_id, params=None):
        path = 'organization/{}/secure_operations/mark_transaction_validated/'
        path = path.format(organization_id)
        return self._post(path, params)

    def mark_sign_and_schedule_transaction(self, organization_id, params=None):
        path = 'organization/{}/secure_operations/mark_sign_and_push/'
        path = path.format(organization_id)
        return self._post(path, params)

    def get_transactions_log(self, organization_id, params=None):
        path = 'organization/{}/transactions_log/'
        path = path.format(organization_id)
        return self._get(path, params)

    def download_transaction_log_csv_file(self, organization_id, params=None):
        path = 'organization/{}/transactions_log/csv/'
        path = path.format(organization_id)
        return self._get(path, params)

    def download_transaction_log_v2_csv_file(self, organization_id, params=None):
        path = 'organization/{}/transactions_log_v2/csv/'
        path = path.format(organization_id)
        return self._get(path, params)

    def list_transaction_rules_for_wallet(self, organization_id, wallet_id, params=None):
        path = 'organization/{}/wallet/{}/policy/transaction_policy_rule/'
        path = path.format(organization_id, wallet_id)
        return self._get(path, params)

    def create_transaction_rule_for_wallet(self, organization_id, wallet_id, params=None):
        path = 'organization/{}/wallet/{}/policy/transaction_policy_rule/create_new/'
        path = path.format(organization_id, wallet_id)
        return self._post(path, params)

    def get_transaction_rule_for_wallet(self, organization_id, wallet_id, transaction_policy_rule_id, params=None):
        path = 'organization/{}/wallet/{}/policy/transaction_policy_rule/{}/'
        path = path.format(organization_id, wallet_id, transaction_policy_rule_id)
        return self._get(path, params)

    def delete_transaction_rule_for_wallet(self, organization_id, wallet_id, transaction_policy_rule_id, params=None):
        path = 'organization/{}/wallet/{}/policy/transaction_policy_rule/{}/'
        path = path.format(organization_id, wallet_id, transaction_policy_rule_id)
        return self._delete(path, params)

    def list_transaction_rules_for_wallet_group(self, organization_id, wallet_group_id, params=None):
        path = 'organization/{}/wallet_group/{}/policy/transaction_policy_rule/'
        path = path.format(organization_id, wallet_group_id)
        return self._get(path, params)

    def create_transaction_rule_for_wallet_group(self, organization_id, wallet_group_id, params=None):
        path = 'organization/{}/wallet_group/{}/policy/transaction_policy_rule/create_new/'
        path = path.format(organization_id, wallet_group_id)
        return self._post(path, params)

    def get_transaction_rule_for_wallet_group(self, organization_id, wallet_group_id, transaction_policy_rule_id, params=None):
        path = 'organization/{}/wallet_group/{}/policy/transaction_policy_rule/{}/'
        path = path.format(organization_id, wallet_group_id, transaction_policy_rule_id)
        return self._get(path, params)

    def list_users(self, organization_id, params=None):
        path = 'organization/{}/all_users/'
        path = path.format(organization_id)
        return self._get(path, params)

    def get_user(self, organization_id, user, params=None):
        path = 'organization/{}/all_users/{}/'
        path = path.format(organization_id, user)
        return self._get(path, params)

    def list_organization_users(self, organization_id, params=None):
        path = 'organization/{}/user/'
        path = path.format(organization_id)
        return self._get(path, params)

    def get_organization_user_by_email(self, organization_id, params=None):
        path = 'organization/{}/user/get_organization_user_by_email/'
        path = path.format(organization_id)
        return self._post(path, params)

    def get_user_information(self, organization_id, user, params=None):
        path = 'organization/{}/user/{}/'
        path = path.format(organization_id, user)
        return self._get(path, params)

    def list_user_groups(self, organization_id, params=None):
        path = 'organization/{}/user_group/'
        path = path.format(organization_id)
        return self._get(path, params)

    def get_user_group_information(self, organization_id, user_group_id, params=None):
        path = 'organization/{}/user_group/{}/'
        path = path.format(organization_id, user_group_id)
        return self._get(path, params)

    def list_user_group_members(self, organization_id, user_group_id, params=None):
        path = 'organization/{}/user_group/{}/group_members/'
        path = path.format(organization_id, user_group_id)
        return self._get(path, params)

    def list_wallets(self, organization_id, params=None):
        path = 'organization/{}/wallet/'
        path = path.format(organization_id)
        return self._get(path, params)

    def create_wallet(self, organization_id, params=None):
        path = 'organization/{}/wallet/create_new/'
        path = path.format(organization_id)
        return self._post(path, params)

    def get_wallet(self, organization_id, wallet_id, params=None):
        path = 'organization/{}/wallet/{}/'
        path = path.format(organization_id, wallet_id)
        return self._get(path, params)

    def get_max_withdrawable_funds(self, organization_id, wallet_id, params=None):
        path = 'organization/{}/wallet/{}/get_max_withdrawable_funds/'
        path = path.format(organization_id, wallet_id)
        return self._post(path, params)

    def list_incoming_transactions(self, organization_id, wallet_id, params=None):
        path = 'organization/{}/wallet/{}/incoming_transactions/'
        path = path.format(organization_id, wallet_id)
        return self._get(path, params)

    def get_incoming_transaction(self, organization_id, wallet_id, incoming_transaction_id, params=None):
        path = 'organization/{}/wallet/{}/incoming_transactions/{}/'
        path = path.format(organization_id, wallet_id, incoming_transaction_id)
        return self._get(path, params)

    def set_wallet_visibility(self, organization_id, wallet_id, params=None):
        path = 'organization/{}/wallet/{}/set_visibility/'
        path = path.format(organization_id, wallet_id)
        return self._post(path, params)

    def list_wallet_membership(self, organization_id, wallet_id, params=None):
        path = 'organization/{}/wallet/{}/wallet_group/'
        path = path.format(organization_id, wallet_id)
        return self._get(path, params)

    def list_wallet_groups(self, organization_id, params=None):
        path = 'organization/{}/wallet_group/'
        path = path.format(organization_id)
        return self._get(path, params)

    def get_wallet_group_information(self, organization_id, wallet_group_id, params=None):
        path = 'organization/{}/wallet_group/{}/'
        path = path.format(organization_id, wallet_group_id)
        return self._get(path, params)

    def list_wallet_group_members(self, organization_id, wallet_group_id, params=None):
        path = 'organization/{}/wallet_group/{}/wallet_group_members/'
        path = path.format(organization_id, wallet_group_id)
        return self._get(path, params)

    def add_wallet_to_wallet_group(self, organization_id, wallet_group_id, params=None):
        path = 'organization/{}/wallet_group/{}/wallet_group_members/create_new/'
        path = path.format(organization_id, wallet_group_id)
        return self._post(path, params)

    def remove_wallet_from_wallet_group(self, organization_id, wallet_group_id, wallet_id, params=None):
        path = 'organization/{}/wallet_group/{}/wallet_group_members/{}/'
        path = path.format(organization_id, wallet_group_id, wallet_id)
        return self._delete(path, params)

    def list_wallet_addresses(self, organization_id, wallet_id, params=None):
        path = 'organization/{}/wallet/{}/wallet_address/'
        path = path.format(organization_id, wallet_id)
        return self._get(path, params)

    def create_wallet_address(self, organization_id, wallet_id, params=None):
        path = 'organization/{}/wallet/{}/wallet_address/create_new/'
        path = path.format(organization_id, wallet_id)
        return self._post(path, params)

    def get_wallet_address(self, organization_id, wallet_id, wallet_address_id, params=None):
        path = 'organization/{}/wallet/{}/wallet_address/{}/'
        path = path.format(organization_id, wallet_id, wallet_address_id)
        return self._get(path, params)

    def rename_wallet_address(self, organization_id, wallet_id, wallet_address_id, params=None):
        path = 'organization/{}/wallet/{}/wallet_address/{}/rename/'
        path = path.format(organization_id, wallet_id, wallet_address_id)
        return self._post(path, params)

    def set_wallet_address_visibility(self, organization_id, wallet_id, wallet_address_id, params=None):
        path = 'organization/{}/wallet/{}/wallet_address/{}/set_visibility/'
        path = path.format(organization_id, wallet_id, wallet_address_id)
        return self._post(path, params)

    def list_wallet_rules_for_wallet(self, organization_id, wallet_id, params=None):
        path = 'organization/{}/wallet/{}/policy/wallet_policy_rule/'
        path = path.format(organization_id, wallet_id)
        return self._get(path, params)

    def create_wallet_rule_for_wallet(self, organization_id, wallet_id, params=None):
        path = 'organization/{}/wallet/{}/policy/wallet_policy_rule/create_new/'
        path = path.format(organization_id, wallet_id)
        return self._post(path, params)

    def get_wallet_rule_for_wallet(self, organization_id, wallet_id, wallet_policy_rule_id, params=None):
        path = 'organization/{}/wallet/{}/policy/wallet_policy_rule/{}/'
        path = path.format(organization_id, wallet_id, wallet_policy_rule_id)
        return self._get(path, params)

    def delete_wallet_rule_for_wallet(self, organization_id, wallet_id, wallet_policy_rule_id, params=None):
        path = 'organization/{}/wallet/{}/policy/wallet_policy_rule/{}/'
        path = path.format(organization_id, wallet_id, wallet_policy_rule_id)
        return self._delete(path, params)

    def list_wallet_rules_for_wallet_group(self, organization_id, wallet_group_id, params=None):
        path = 'organization/{}/wallet_group/{}/policy/wallet_policy_rule/'
        path = path.format(organization_id, wallet_group_id)
        return self._get(path, params)

    def create_wallet_rule_for_wallet_group(self, organization_id, wallet_group_id, params=None):
        path = 'organization/{}/wallet_group/{}/policy/wallet_policy_rule/create_new/'
        path = path.format(organization_id, wallet_group_id)
        return self._post(path, params)

    def get_wallet_rule_for_wallet_group(self, organization_id, wallet_group_id, wallet_policy_rule_id, params=None):
        path = 'organization/{}/wallet_group/{}/policy/wallet_policy_rule/{}/'
        path = path.format(organization_id, wallet_group_id, wallet_policy_rule_id)
        return self._get(path, params)

    def get_debug_information(self, params=None):
        path = 'debug/'
        path = path.format()
        return self._get(path, params)

    def synchronous_push_for_black_box_xdr_mainnet(self, params=None):
        path = 'stellar-mainnet/push_signed_content/'
        path = path.format()
        return self._post(path, params)

    def synchronous_push_for_black_box_xdr_testnet(self, params=None):
        path = 'stellar-testnet/push_signed_content/'
        path = path.format()
        return self._post(path, params)
        
    # Getter and Setter
    
    def _get_base_url(self):
        return self.__base_url
    
    def _get_jwt(self):
        return self.__jwt
    
    def _get_requests_session(self):
        return self.__requests_session
    
    def _get_response(self):
        return self.__response
    
    def _set_response(self, response):
        self.__response = response
        