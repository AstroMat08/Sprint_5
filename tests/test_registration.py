import pytest
from selenium.webdriver.support import expected_conditions
from ..data.locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators
from ..helpers.generator import generate_email, generate_password, generate_name

class TestRegistration:
    
    def test_successful_registration(self, driver, wait):
        """Тест успешной регистрации"""
        # Генерируем данные для пользователя
        email = generate_email()
        password = generate_password()
        name = generate_name()
        
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Переход на страницу регистрации
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
        
        # Заполнение полей
        wait.until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)).send_keys(name)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)
        
        # Клик на "Зарегистрироваться"
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        # Проверка: появилась кнопка "Войти" на странице входа
        wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()
    
    def test_registration_invalid_password_error(self, driver, wait):
        """Тест ошибки для пароля короче 6 символов"""
        email = generate_email()
        name = generate_name()
        
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Переход на страницу регистрации
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
        
        # Заполнение полей с коротким паролем (5 символов)
        wait.until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)).send_keys(name)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("12345")
        
        # Клик на "Зарегистрироваться"
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        # Проверка появления ошибки
        wait.until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR))
        assert driver.find_element(*RegistrationPageLocators.PASSWORD_ERROR).is_displayed()