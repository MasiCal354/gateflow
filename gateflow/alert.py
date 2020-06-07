from slack_webhook import Slack
from .exceptions import InputException

class BaseAlert:
    def __init__(self, credentials=None, message=None, destinations=None):
        self.__credentials = credentials
        self.__message = message
        self.__destination = destination
    
    def send(self):
        pass
    
    def get_credentials(self):
        return self.__credentials
    
    def get_message(self):
        return self.__message
    
    def get_destination(self):
        return self.__destination
    
    def set_credentials(self, credentials):
        self.__credentials = credentials
    
    def set_message(self, message):
        self.__message = message
        
    def set_destination(self, destination):
        self.__destination = destination
    
class SlackAlert(BaseAlert):
    """
    credentials = None
    messages = payload # json object/dict with mandatory 'text' key and optional 'attachments' key
    destination = webhook_url
    """
    def send(self):
        webhook_url = self.get_destination()
        payload = self.get_messages()
        slack = Slack(url=webhook_url)
        if 'text' not in payload.keys():
            expression = payload
            messages = 'text key not exist on payload input'
            raise InputExpression(expression, messages)
        elif 'attachments' not in payload.keys():
            slack.post(text = payload['text'])
        else:
            slack.post(text = payload['text'], attachments = payload['attachments'])
        
    
class TelegramAlert(BaseAlert):
    def send(self):
        pass