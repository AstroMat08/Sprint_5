import pytest
from selenium.webdriver.support import expected_conditions
from ..data.locators import MainPageLocators, PersonalAccountLocators

class TestPersonalAccount:
    
    def test_go_to_personal_account(self, auth_user, wait):
        """Тест перехода в личный кабинет по клику на 'Личный кабинет'"""
        driver = auth_user
        
        # Клик на "Личный кабинет"
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        
        # Проверка: появилась кнопка "Выйти"
        wait.until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON))
        assert driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).is_displayed()
    
    def test_go_to_constructor_from_account(self, auth_user, wait):
        """Тест перехода из личного кабинета в конструктор по клику на 'Конструктор'"""
        driver = auth_user
        
        # Переход в личный кабинет
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON))
        
        # Клик на "Конструктор"
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_LINK)).click()
        
        # Проверка: появилась кнопка "Оформить заказ"
        wait.until(expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).is_displayed()
    
    def test_go_to_constructor_from_account_logo(self, auth_user, wait):
        """Тест перехода из личного кабинета в конструктор по клику на логотип"""
        driver = auth_user
        
        # Переход в личный кабинет
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON))
        
        # Клик на логотип
        wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGO_LINK)).click()
        
        # Проверка: появилась кнопка "Оформить заказ"
        wait.until(expected_conditions.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        assert driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).is_displayed()