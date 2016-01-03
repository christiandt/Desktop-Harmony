import logging
from harmony import auth
from harmony import client


class Controller():

    def __init__(self, username, password, ip, port):
        logging.basicConfig()
        self.logger = logging.getLogger()
        
        self.username = username
        self.password = password
        self.ip = ip
        self.port = port

    def login(self):
        self.token = auth.login(self.username, self.password)
        if not self.token:
            raise Exception('Could not log in to the harmony service')
        session_token = auth.swap_auth_token(self.ip, self.port, self.token)
        self.harmony_client = client.create_and_connect_client(self.ip, self.port, self.token)
        if not self.harmony_client:
            raise Exception('Could not log in to the harmony device')

    def get_activities(self):
        configuration = self.harmony_client.get_config()
        return configuration['activity']

    def start_activity(self, selected_id):
        self.harmony_client.start_activity(selected_id)

    def disconnect(self):
        self.harmony_client.disconnect(send_close=True)
