import allure
from api.endpoint.base_method import BaseMethod


class Registration(BaseMethod):

    def __init__(self, email, password):
        super().__init__()
        self.email = email
        self.password = password

    def create_new_user(self):
        with allure.step('Send request to create user'):
            self.response = self.post_request_create_user(
                self.email, self.password
            )
            return self.response

    def returned_message_invalid_email_address(self):
        with allure.step('Check response message'):
            response_data = self.response.json()
            message = response_data['message']
            return message == 'Invalid email address'

    def returned_message_invalid_password(self):
        with allure.step('Check response message'):
            response_data = self.response.json()
            message = response_data['message']
            return message == 'Invalid password. The password must' \
                              ' be typed in Latin letters, consist of' \
                              ' at least 8 characters and contain at' \
                              ' least one lowercase and one uppercase' \
                              ' character'

    def returned_message_invalid_email_and_password(self):
        with allure.step('Check response message'):
            response_data = self.response.json()
            message = response_data['message']
            return message == 'Invalid email and password. The password' \
                              ' must be typed in Latin letters, consist of' \
                              ' at least 8 characters and contain at least one' \
                              ' lowercase and one uppercase character'

    def returned_message_user_exists(self):
        with allure.step('Check response message'):
            response_data = self.response.json()
            message = response_data['message']
            return message == 'User with this email is already exists'
