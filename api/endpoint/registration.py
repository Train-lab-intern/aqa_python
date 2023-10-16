import allure
from api.endpoint.base_method import BaseMethod


class Registration(BaseMethod):

    def __init__(self, email, username, password):
        super().__init__()
        self.response = None
        self.email = email
        self.username = username
        self.password = password

    def create_new_user(self):
        with allure.step('Send request to create user'):
            self.response = self.post_request_create_user(
                self.email, self.username, self.password
            )
            return self.response

    def returned_200(self):
        with allure.step('Check status code 200'):
            return self.response.status_code == 200

    def returned_text_registration_initiated(self):
        with allure.step('Check response text'):
            return self.response.text == 'Registration initiated.' \
                                        ' Please check your email for further instructions.'

    def returned_text_registration_completed(self):
        with allure.step('Check response text'):
            return self.response.text == 'Registration completed successfully!'

    def returned_message_invalid_email_address(self):
        with allure.step('Check response message'):
            response_data = self.response.json()
            message = response_data['message']
            return message == 'Invalid email address'

    def returned_message_email_must_be_between_8_and_256_characters(self):
        with allure.step('Check response message'):
            response_data = self.response.json()
            message = response_data['message']
            return message == 'User email must be between 8 and 256 characters'

    def returned_message_user_exists(self):
        with allure.step('Check response message'):
            response_data = self.response.json()
            message = response_data['message']
            return message == 'User with this username is already exists.'

    def returned_message_user_mot_found(self, email):
        with allure.step('Check response message'):
            response_data = self.response.json()
            message = response_data['message']
            return message == f'User not found with email: {email}'

    def returned_status_bad_request(self):
        with allure.step('Check response status'):
            response_data = self.response.json()
            status = response_data['status']
            return status == 'BAD_REQUEST'

    def returned_400(self):
        with allure.step('Check status code 400'):
            return self.response.status_code == 400

    def confirm_registration(self, email):
        with allure.step('Send request confirm registration'):
            self.response = self.get_request_confirm_registration(email)
            return self.response
