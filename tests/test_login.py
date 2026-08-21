import pytest
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, LoginPageLocators
from helpers.generator import generate_email, generate_password


class TestLogin:
    
    def test_login_from_main_page(self, driver, wait, test_user):
        """Тест входа по кнопке 'Войти в аккаунт' на главной"""
        driver.get("https://stellarburgers.nomoreparties.site/")
        
        # Клик на "Войти в аккаунт"
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        
        # Ввод email и пароля
        wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(test_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_user['password'])
        
        # Клик на "Войти"
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверка: появилась кнопка "Оформить заказ"
        wait.until(expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).is_displayed()
    
    def test_login_from_personal_account(self, driver, wait, test_user):
        """Тест входа через кнопку 'Личный кабинет'"""
        driver.get("https://stellarburgers.nomoreparties.site/")
        
        # Клик на "Личный кабинет"
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        
        # Ввод email и пароля
        wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(test_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_user['password'])
        
        # Клик на "Войти"
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверка: появилась кнопка "Оформить заказ"
        wait.until(expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).is_displayed()
    
    def test_login_from_registration_form(self, driver, wait, test_user):
        """Тест входа через кнопку в форме регистрации"""
        driver.get("https://stellarburgers.nomoreparties.site/")
        
        # Переход на страницу регистрации
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
        
        # Клик на ссылку "Войти" на странице регистрации
        wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()
        
        # Ввод email и пароля
        wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(test_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_user['password'])
        
        # Клик на "Войти"
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверка: появилась кнопка "Оформить заказ"
        wait.until(expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).is_displayed()
    
    def test_login_from_password_recovery(self, driver, wait, test_user):
        """Тест входа через кнопку в форме восстановления пароля"""
        driver.get("https://stellarburgers.nomoreparties.site/")
        
        # Переход на страницу восстановления пароля
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK)).click()
        
        # Клик на ссылку "Войти"
        wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()
        
        # Ввод email и пароля
        wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(test_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_user['password'])
        
        # Клик на "Войти"
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        # Проверка: появилась кнопка "Оформить заказ"
        wait.until(expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).is_displayed()