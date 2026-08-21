import pytest
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators

TEST_EMAIL = "matvey_kozlov_53_888@yandex.ru"
TEST_PASSWORD = "12345678"
TEST_NAME = "Matvey"

class TestRegistration:
    
    def test_successful_registration(self, driver, wait):
        """Тест успешной регистрации"""
        driver.get("https://stellarburgers.nomoreparties.site/")
        
        # Переход на страницу регистрации
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
        
        # Заполнение полей
        wait.until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)).send_keys(TEST_NAME)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(TEST_PASSWORD)
        
        # Клик на "Зарегистрироваться"
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        # Проверка: появилась кнопка "Войти" на странице входа
        wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()
    
    def test_registration_invalid_password_error(self, driver, wait):
        """Тест ошибки для пароля короче 6 символов"""
        driver.get("https://stellarburgers.nomoreparties.site/")
        
        # Переход на страницу регистрации
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
        
        # Заполнение полей с коротким паролем
        wait.until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)).send_keys(TEST_NAME)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(TEST_EMAIL)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("12345")
        
        # Клик на "Зарегистрироваться"
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        # Проверка появления ошибки
        wait.until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR))
        assert driver.find_element(*RegistrationPageLocators.PASSWORD_ERROR).is_displayed()