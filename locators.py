from selenium.webdriver.common.by import By
from data import advertisement



# Основные кнопки
LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonSecondary') and contains(text(), 'Вход и регистрация')]")
CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
NO_ACCOUNT_BUTTON = (By.XPATH, '//button[contains(text(), "Нет аккаунта")]')
AVATAR_BUTTON = (By.CSS_SELECTOR, "button.circleSmall")

# Форма входа/регистрации
EMAIL_INPUT = (By.XPATH, "//input[@class='input_inputStandart__JweLZ spanGlobal' and @placeholder='Введите Email']")
PASSWORD_INPUT = (By.XPATH, "//input[@class='input_inputStandart__JweLZ spanGlobal' and @placeholder='Пароль']")
CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Повторите пароль']")

# Аватар и имя пользователя 
ICON_USER = (By.XPATH, '//button[@class="circleSmall"]')
NAME_USER = (By.XPATH, "//h3[contains(@class, 'profileText name')]")

# Заголовок и элементы управления
TITLE = (By.CSS_SELECTOR, ".popUp_titleRow__M7tGg .h1")
CLOSE_BUTTON = (By.CSS_SELECTOR, ".popUp_XBtn__uEWoB")
    
# Ошибки валидации
LABEL_ERR = (By.XPATH, "//span[@class='input_span__yWPqB' and text()='Ошибка']")
EMAIL_ERR_FIELD = (By.CSS_SELECTOR, "div.popUp_inputColumn__RgD8n div:nth-child(1) .input_invalid")
PASS_ERR_FIELD = (By.CSS_SELECTOR, "div.popUp_inputColumn__RgD8n div:nth-child(2) .input_invalid")
CONFIRM_ERR_FIELD = (By.CSS_SELECTOR, "div.popUp_inputColumn__RgD8n div:nth-child(3) .input_invalid")
ERR_MESSAGE = (By.XPATH, "//*[contains(text(), 'Пароли не совпадают')]") 
   
# Создание объявления
BUTTON_CREATE_AD = (By.XPATH, "//button[contains(@class, 'buttonPrimary') and contains(., 'Разместить объявление')]")
INPUT_TITLE = (By.XPATH, "//input[@placeholder='Название']")
INPUT_DESCRIPTION = (By.XPATH, "//textarea[@placeholder='Описание товара']")
INPUT_PRICE = (By.CSS_SELECTOR, "input[name='price']")
BUTTON_PUBLISH = (By.XPATH, "//button[text()='Опубликовать']")
DROPDOWN_CATEGORY = (By.XPATH, ".//button[contains(@class, 'dropDownMenu_arrowDown')]")
SELECT_CATEGORY = (By.XPATH, '//span[text()="Книги"]/parent::button[starts-with(@class, "dropDownMenu_btn")]')
DROPDOWN_CITY = (By.XPATH, "//input[@name='city']/following-sibling::button")
SELECT_CITY = (By.XPATH, f'//button[.//span[text()="Казань"]]')
RADIO_CONDITION = (By.CSS_SELECTOR, 'div.radioUnput_shell__Wtdwe input[value="Б/У"] + div.radioUnput_inputRegular__FbVbr')
SECTION_MY_ADS = (By.XPATH, "//h1[text()='Мои объявления']")
ITEM_AD = (By.XPATH, "(//div[contains(@class, 'card')])[last()]")
NOTIFICATION_MODAL = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
NEXT_PAGE_BUTTON = (By.XPATH, "//button[contains(@class, 'arrowButton--right') and not(@disabled)]")
NEXT_PAGE_DISABLED = (By.XPATH, "//button[contains(@class, 'arrowButton--right') and @disabled]")