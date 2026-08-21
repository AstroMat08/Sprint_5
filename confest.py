import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators
from helpers.generator import generate_email, generate_password, generate_name

BASE_URL = "https://stellarburgers.nomoreparties.site/"

@pytest.fixture
def driver():
    """Фикстура для создания драйвера Chrome"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit() 

@pytest.fixture
def wait(driver):
    """Фикстура для явного ожидания"""
    return WebDriverWait(driver, 10)

@pytest.fixture
def main_page(driver):
    """Фикстура для открытия главной страницы"""
    driver.get(BASE_URL)
    return driver

@pytest.fixture
def test_user():
    """
    Фикстура для создания тестового пользователя с уникальными данными
    """
    return {
        'email': generate_email(),
        'password': generate_password(),
        'name': generate_name()
    }

@pytest.fixture
def auth_user(driver, wait, test_user):
    """
    Фикстура для авторизованного пользователя
    Создает нового пользователя и авторизует его
    """
    # Сначала регистрируем пользователя
    driver.get(BASE_URL)
    
    # Переход на страницу регистрации
    wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
    wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
    
    # Заполнение полей регистрации
    wait.until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)).send_keys(test_user['name'])
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(test_user['email'])
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(test_user['password'])
    
    # Клик на "Зарегистрироваться"
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    
    # Ожидание перехода на страницу входа
    wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
    
    # Теперь авторизуемся
    wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(test_user['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_user['password'])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    
    # Ожидание загрузки главной страницы
    wait.until(expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
    
    # Сохраняем данные пользователя в driver для доступа в тестах
    driver.test_user = test_user
    
    return driver