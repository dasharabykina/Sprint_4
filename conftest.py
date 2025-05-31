import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from urls import *
from data import Login_Exist_User
import random


@pytest.fixture
def driver():
    options = Options()
    service = Service (executable_path='D:\\WebDriver\\bin\\chromedriver.exe')
    options.add_argument('window-size=1920,1080')
    driver = webdriver.Chrome(service = service, options = options)
    yield driver
    driver.quit()

@pytest.fixture
def create_email():
    fake = Faker()
    return fake.email()

@pytest.fixture
def create_password():
    fake = Faker()
    return fake.password(length=10)

@pytest.fixture
def open_main_page(driver):
    driver.get(BASE_URL)

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)

@pytest.fixture
def login(driver, open_main_page, wait):
    wait.until(EC.element_to_be_clickable(LOGIN_REGISTER_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(Login_Exist_User.exist_user_mail)
    driver.find_element(*PASSWORD_INPUT).send_keys(Login_Exist_User.exist_user_pass)
    driver.find_element(*LOGIN_BUTTON).click()

@pytest.fixture
def generate_product_name():
    # Генерация случайного названия продукта
    product_name = f'Ручка {random.randint(100, 999)}'
    return product_name