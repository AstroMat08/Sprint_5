from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы главной страницы"""
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Кнопка "Оформить заказ"
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Ссылка "Конструктор"
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    # Логотип Stellar Burgers
    LOGO_LINK = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a")

class LoginPageLocators:
    """Локаторы страницы входа"""
    # Поле ввода Email
    EMAIL_INPUT = (By.XPATH, "//input[@type='text' and @name='name']")
    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    # Ссылка "Восстановить пароль"
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

class RegistrationPageLocators:
    """Локаторы страницы регистрации"""
    # Поле ввода имени
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле ввода Email
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Ошибка для некорректного пароля
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")

class PersonalAccountLocators:
    """Локаторы личного кабинета"""
    # Профиль
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    # Кнопка "Выйти"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    # Имя пользователя
    USER_NAME = (By.XPATH, "//p[text()='Имя']/following-sibling::p")

class ConstructorLocators:
    """Локаторы раздела Конструктор"""
    # Раздел "Булки"
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    # Раздел "Соусы"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    # Раздел "Начинки"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    # Активный таб
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'current')]/span")