from locators import *
from urls import *
from conftest import *

from selenium.webdriver.support import expected_conditions as EC
from data import Login_Exist_User


class TestLogin:
    def test_successful_login_with_valid_credentials(self, driver, open_main_page, wait):

        wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(Login_Exist_User.exist_user_mail)
        driver.find_element(*PASSWORD_INPUT).send_keys(Login_Exist_User.exist_user_pass)
        driver.find_element(*LOGIN_BUTTON).click()
    
        user_name = wait.until(EC.visibility_of_element_located(NAME_USER)).text
        user_icon = wait.until(EC.visibility_of_element_located(ICON_USER))

        assert user_name.rstrip('.') == "User" and user_icon.is_displayed()
