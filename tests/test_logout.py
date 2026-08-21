import pytest
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, PersonalAccountLocators, LoginPageLocators

class TestLogout:
    
    def test_logout_from_account(self, auth_user, wait):
        """Тест выхода по кнопке 'Выйти' в личном кабинете"""
        driver = auth_user
        
        # Переход в личный кабинет
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON))
        
        # Клик на "Выйти"
        wait.until(expected_conditions.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON)).click()
        
        # Проверка: появилась кнопка "Войти" на странице входа
        wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON).is_displayed()