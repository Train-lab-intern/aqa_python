import allure
from api.endpoint.base_method import BaseMethod


class Authentication(BaseMethod):

    def __init__(self, login, password):
        super().__init__()
        self.response = None
        self.login = login
        self.password = password

    def authentication(self):
        with allure.step('Send a login request'):
            self.response = self.post_request_authentication(self.login, self.password)
            return self.response

    def returned_message_invalid_login_or_password(self):
        with allure.step('Check response message'):
            response_data = self.response.json()
            message = response_data['message']
            return message == 'Invalid login or password'
