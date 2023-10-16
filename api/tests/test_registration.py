import pytest
import allure
from api.endpoint.registration import Registration
import test_data


@allure.feature('Registration')
@allure.story('Send a request with a valid email')
@pytest.mark.parametrize('email', test_data.VALID_EMAILS)
def test_check_valid_emails(connect_db, email, check_existence_and_delete_email):
    register_endpoint = Registration(email, test_data.USERNAME, test_data.PASSWORD)
    register_endpoint.create_new_user()
    assert register_endpoint.returned_200()
    assert register_endpoint.returned_text_registration_initiated()


@allure.feature('Registration')
@allure.story('Send a request with an invalid email address')
@pytest.mark.parametrize('email', test_data.INVALID_EMAILS)
def test_check_invalid_emails(connect_db, email, check_existence_and_delete_email):
    register_endpoint = Registration(email, test_data.USERNAME, test_data.PASSWORD)
    register_endpoint.create_new_user()
    assert register_endpoint.returned_400()
    assert register_endpoint.returned_message_invalid_email_address()
    assert register_endpoint.returned_status_bad_request()


@allure.feature('Registration')
@allure.story('Check username')
@pytest.mark.parametrize('username', test_data.USERNAMES)
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_username(connect_db, username, check_existence_and_delete_email, email):
    register_endpoint = Registration(email, username, test_data.PASSWORD)
    register_endpoint.create_new_user()
    assert register_endpoint.returned_200()
    assert register_endpoint.returned_text_registration_initiated()


@allure.feature('Registration')
@allure.story('Send a request with an valid password')
@pytest.mark.parametrize('password', test_data.VALID_PASSWORD)
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_valid_password(connect_db, password, email, check_existence_and_delete_email):
    register_endpoint = Registration(email, test_data.USERNAME, password)
    register_endpoint.create_new_user()
    assert register_endpoint.returned_200()
    assert register_endpoint.returned_text_registration_initiated()


@allure.feature('Registration')
@allure.story('Send a request with an invalid password')
@pytest.mark.parametrize('password', test_data.INVALID_PASSWORD)
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_invalid_password(connect_db, password, email, check_existence_and_delete_email):
    register_endpoint = Registration(email, test_data.USERNAME, password)
    register_endpoint.create_new_user()
    assert register_endpoint.returned_400()
    assert register_endpoint.returned_status_bad_request()


@allure.feature('Registration')
@allure.story('Send a request with empty fields')
def test_registration_with_empty_fields(connect_db):
    register_endpoint = Registration(
        test_data.EMPTY_FIELD, test_data.EMPTY_FIELD, test_data.EMPTY_FIELD
    )
    register_endpoint.create_new_user()
    assert register_endpoint.returned_400()
    assert register_endpoint.returned_status_bad_request()


@allure.feature('Registration')
@allure.story('Send a request with empty username and password')
def test_registration_with_empty_username_and_password(connect_db):
    register_endpoint = Registration(
        test_data.EMAIL, test_data.EMPTY_FIELD, test_data.EMPTY_FIELD
    )
    register_endpoint.create_new_user()
    assert register_endpoint.returned_400()
    assert register_endpoint.returned_status_bad_request()


@allure.feature('Registration')
@allure.story('Send a request with empty email and password')
def test_registration_with_empty_email_and_password(connect_db):
    register_endpoint = Registration(
        test_data.EMPTY_FIELD, test_data.USERNAME, test_data.EMPTY_FIELD
    )
    register_endpoint.create_new_user()
    assert register_endpoint.returned_400()
    assert register_endpoint.returned_status_bad_request()


@allure.feature('Registration')
@allure.story('Send a request with empty username and email')
def test_registration_with_empty_username_and_email(connect_db):
    register_endpoint = Registration(
        test_data.EMPTY_FIELD, test_data.EMPTY_FIELD, test_data.PASSWORD
    )
    register_endpoint.create_new_user()
    assert register_endpoint.returned_400()
    assert register_endpoint.returned_status_bad_request()
    assert register_endpoint.returned_message_email_must_be_between_8_and_256_characters


@allure.feature('Registration')
@allure.story('Send a request with data existing user')
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_registration_with_existing_user(connect_db, check_existence_and_delete_email, email):
    register_endpoint = Registration(email, test_data.USERNAME, test_data.PASSWORD)
    register_endpoint.create_new_user()
    register_endpoint.create_new_user()
    assert register_endpoint.returned_400()
    assert register_endpoint.returned_status_bad_request()
    assert register_endpoint.returned_message_user_exists()


@allure.feature('Registration')
@allure.story('Send a request confirm registration')
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_confirm_registration(
        connect_db, check_existence_and_delete_email, email, delete_session
):
    register_endpoint = Registration(
        email, test_data.USERNAME, test_data.PASSWORD
    )
    register_endpoint.create_new_user()
    register_endpoint.confirm_registration(email)
    assert register_endpoint.returned_200()
    assert register_endpoint.returned_text_registration_completed()


@allure.feature('Registration')
@allure.story('Send a request confirm registration')
@pytest.mark.parametrize('email', [test_data.EMAIL])
def test_confirm_registration_with_invalid_email(
        connect_db, check_existence_and_delete_email, email, delete_session
):
    register_endpoint = Registration(email, test_data.USERNAME, test_data.PASSWORD)
    register_endpoint.create_new_user()
    register_endpoint.confirm_registration(test_data.NON_EXISTENT_EMAIL)
    assert register_endpoint.returned_400()
    assert register_endpoint.returned_status_bad_request()
    assert register_endpoint.returned_message_user_mot_found(test_data.NON_EXISTENT_EMAIL)
