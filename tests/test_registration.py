from locators import *
from selenium.webdriver.support import expected_conditions as EC
from data import Invalid_email_shows_error, Login_Exist_User


class TestRegistration:
    def test_successful_registration_with_valid_data(self, driver, open_main_page, wait, create_email,create_password):
        email = create_email
        password = create_password
        wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(email)
        driver.find_element(*PASSWORD_INPUT).send_keys(password)
        driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(password)
        wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)).click()
        user_name = wait.until(EC.visibility_of_element_located(NAME_USER)).text
        user_icon = wait.until(EC.visibility_of_element_located(ICON_USER))
        assert user_name.rstrip('.') == "User" and user_icon.is_displayed()

    def test_register_existing_user_shows_error(self, driver, open_main_page, wait):
        wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(Login_Exist_User.exist_user_mail)
        driver.find_element(*PASSWORD_INPUT).send_keys(Login_Exist_User.exist_user_pass)
        driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(Login_Exist_User.exist_user_pass)
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

        error_msg = wait.until(EC.visibility_of_element_located(LABEL_ERR))
        assert error_msg.text.strip() == "Ошибка"
        

    def test_registration_with_invalid_email_shows_error_message(self, driver, open_main_page, wait):
        wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(Invalid_email_shows_error.invalid_mail)
        driver.find_element(*PASSWORD_INPUT).send_keys(Invalid_email_shows_error.password)
        driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(Invalid_email_shows_error.password)
        wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)).click()

        error_msg = wait.until(EC.visibility_of_element_located(LABEL_ERR))
        assert error_msg.text.strip() == "Ошибка"

    def test_password_mismatch_shows_error(self, driver, open_main_page, wait, create_email):
        email = create_email
        wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(email)
        driver.find_element(*PASSWORD_INPUT).send_keys(Invalid_email_shows_error.password)
        driver.find_element(*CONFIRM_PASSWORD_INPUT).send_keys(Invalid_email_shows_error.mismatched_pass)
        wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)).click()

        error_msg = wait.until(EC.visibility_of_element_located(ERR_MESSAGE))

        assert "Пароли не совпадают" in error_msg.text