import json
import requests
import allure
import settings


class BaseMethod:

    def __init__(self):
        self.base_url = settings.BASE_URL
        self.register_user = settings.REGISTER_USER
        self.authentication_url = settings.AUTHENTICATION_URL
        self.response = None

    def post_request_create_user(self, email, password):
        headers = {
            'Content-Type': 'application/json'
        }
        data = json.dumps({
            "email": f"{email}",
            "password": f"{password}"
        })
        request = requests.request('POST', self.base_url + self.register_user, headers=headers,
                                   data=data, timeout=20)
        return request

    def post_request_authentication(self, email, password):
        headers = {
            'Content-Type': 'application/json'
        }
        data = json.dumps({
            "userEmail": f"{email}",
            "userPassword": f"{password}"
        })
        request = requests.request(
            'POST', self.base_url + self.authentication_url, data=data, headers=headers, timeout=20
        )
        return request

    def returned_message_password_field_is_required(self):
        with allure.step('Check response message'):
            response_data = self.response.json()
            message = response_data['message']
            return message == 'The password field is required'

    def returned_message_email_field_is_required(self):
        with allure.step('Check response message'):
            response_data = self.response.json()
            message = response_data['message']
            return message == 'The email field is required'

    def returned_message_email_and_password_fields_are_required(self):
        with allure.step('Check response message'):
            response_data = self.response.json()
            message = response_data['message']
            return message == 'Email and password fields are required'

    def returned_400(self):
        with allure.step('Check status code 400'):
            return self.response.status_code == 400

    def returned_201(self):
        with allure.step('Check status code 200'):
            return self.response.status_code == 201

    def returned_200(self):
        with allure.step('Check status code 200'):
            return self.response.status_code == 200

    def returned_401(self):
        with allure.step('Check status code 401'):
            return self.response.status_code == 401
