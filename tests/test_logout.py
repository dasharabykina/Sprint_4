from locators import *
from urls import *
from conftest import *
from selenium.webdriver.support import expected_conditions as EC


def test_logout_login_button_appears(driver, open_main_page, login, wait):

    wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()

    assert wait.until(EC.visibility_of_element_located(LOGIN_REGISTER_BUTTON)).is_displayed()