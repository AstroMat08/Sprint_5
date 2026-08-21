import pytest
from selenium.webdriver.support import expected_conditions
from ..data.locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators

class TestLogin:
    
    def test_login_from_main_page(self, driver, wait, auth_user):
        """Тест входа по кнопке 'Войти в аккаунт' на главной"""
        test_user = auth_user.test_user
        
        driver.get("https://stellarburgers.education-services.ru/")
        
        # ВХОД
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(test_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        wait.until(expected_conditions.presence_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).is_displayed()
    
    def test_login_from_personal_account(self, driver, wait, auth_user):
        """Тест входа через кнопку 'Личный кабинет'"""
        test_user = auth_user.test_user
        
        driver.get("https://stellarburgers.education-services.ru/")
        
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        
        wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(test_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        wait.until(expected_conditions.presence_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).is_displayed()
    
    def test_login_from_registration_form(self, driver, wait, auth_user):
        """Тест входа через кнопку в форме регистрации"""
        test_user = auth_user.test_user
        
        driver.get("https://stellarburgers.education-services.ru/")
        
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
        
        wait.until(expected_conditions.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT))
        
        # Кликаем на "Войти" на странице регистрации
        wait.until(expected_conditions.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)).click()
        
        wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(test_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        wait.until(expected_conditions.presence_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).is_displayed()
    
    def test_login_from_password_recovery(self, driver, wait, auth_user):
        """Тест входа через кнопку в форме восстановления пароля"""
        test_user = auth_user.test_user
        
        driver.get("https://stellarburgers.education-services.ru/")
        
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
        wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK)).click()
        
        # Кликаем на "Войти" на странице восстановления
        wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON_IN_RECOVERY)).click()
        
        wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(test_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(test_user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        wait.until(expected_conditions.presence_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).is_displayed()