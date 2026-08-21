import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, LoginPageLocators

BASE_URL = "https://stellarburgers.nomoreparties.site/"

# Конкретные данные для аккаунта
TEST_EMAIL = "matvey_kozlov_53_888@yandex.ru"
TEST_PASSWORD = "12345678"
TEST_NAME = "Matvey"

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
def auth_user(driver, wait):
    """Фикстура для авторизованного пользователя"""
    driver.get(BASE_URL)
    
    # Клик на "Войти в аккаунт"
    wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
    
    # Ввод email
    wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(TEST_EMAIL)
    
    # Ввод пароля
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    
    # Клик на "Войти"
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    
    # Ожидание загрузки главной страницы
    wait.until(expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
    
    return driver