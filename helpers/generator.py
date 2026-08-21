import random
import string

def generate_email():
    
    # Фиксированная часть
    name = "matvey_kozlov_53"
    
    # Генерируем 3 случайные цифры
    random_digits = ''.join(random.choices(string.digits, k=3))
    
    # Формируем email
    email = f"{name}_{random_digits}@yandex.ru"
    
    return email

def generate_password():
    """
    Генерирует пароль длиной от 6 до 12 символов
    """
    # Пароль должен содержать буквы и цифры
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choices(chars, k=random.randint(6, 12)))
    return password

def generate_name():
    """
    Генерирует имя
    """
    name = "Матвей"
    return name