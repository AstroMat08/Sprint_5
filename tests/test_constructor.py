import pytest
from selenium.webdriver.support import expected_conditions
from ..data.locators import ConstructorLocators

class TestConstructor:
    
    def test_constructor_buns_tab(self, driver, wait):
        """Тест перехода к разделу 'Булки'"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Ждем загрузки вкладок
        wait.until(expected_conditions.visibility_of_element_located(ConstructorLocators.BUNS_TAB))
        
        # Используем JavaScript для клика (обходит перекрытие)
        buns_tab = driver.find_element(*ConstructorLocators.BUNS_TAB)
        driver.execute_script("arguments[0].scrollIntoView(true);", buns_tab)
        driver.execute_script("arguments[0].click();", buns_tab)
        
        # Проверка: активная вкладка "Булки"
        active_tab = wait.until(expected_conditions.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB))
        assert active_tab.text == "Булки"
    
    def test_constructor_sauces_tab(self, driver, wait):
        """Тест перехода к разделу 'Соусы'"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        wait.until(expected_conditions.visibility_of_element_located(ConstructorLocators.SAUCES_TAB))
        
        sauces_tab = driver.find_element(*ConstructorLocators.SAUCES_TAB)
        driver.execute_script("arguments[0].scrollIntoView(true);", sauces_tab)
        driver.execute_script("arguments[0].click();", sauces_tab)
        
        active_tab = wait.until(expected_conditions.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB))
        assert active_tab.text == "Соусы"
    
    def test_constructor_fillings_tab(self, driver, wait):
        """Тест перехода к разделу 'Начинки'"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        wait.until(expected_conditions.visibility_of_element_located(ConstructorLocators.FILLINGS_TAB))
        
        fillings_tab = driver.find_element(*ConstructorLocators.FILLINGS_TAB)
        driver.execute_script("arguments[0].scrollIntoView(true);", fillings_tab)
        driver.execute_script("arguments[0].click();", fillings_tab)
        
        active_tab = wait.until(expected_conditions.visibility_of_element_located(ConstructorLocators.ACTIVE_TAB))
        assert active_tab.text == "Начинки"