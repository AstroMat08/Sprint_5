import pytest
from selenium.webdriver.support import expected_conditions
from locators import ConstructorLocators

class TestConstructor:
    
    def test_constructor_buns_tab(self, driver, wait):
        """Тест перехода к разделу 'Булки'"""
        driver.get("https://stellarburgers.nomoreparties.site/")
        
        # Клик на раздел "Булки"
        wait.until(expected_conditions.element_to_be_clickable(ConstructorLocators.BUNS_TAB)).click()
        
        # Проверка: активная вкладка "Булки"
        active_tab = wait.until(expected_conditions.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB))
        assert active_tab.text == "Булки"
    
    def test_constructor_sauces_tab(self, driver, wait):
        """Тест перехода к разделу 'Соусы'"""
        driver.get("https://stellarburgers.nomoreparties.site/")
        
        # Клик на раздел "Соусы"
        wait.until(expected_conditions.element_to_be_clickable(ConstructorLocators.SAUCES_TAB)).click()
        
        # Проверка: активная вкладка "Соусы"
        active_tab = wait.until(expected_conditions.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB))
        assert active_tab.text == "Соусы"
    
    def test_constructor_fillings_tab(self, driver, wait):
        """Тест перехода к разделу 'Начинки'"""
        driver.get("https://stellarburgers.nomoreparties.site/")
        
        # Клик на раздел "Начинки"
        wait.until(expected_conditions.element_to_be_clickable(ConstructorLocators.FILLINGS_TAB)).click()
        
        # Проверка: активная вкладка "Начинки"
        active_tab = wait.until(expected_conditions.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB))
        assert active_tab.text == "Начинки"