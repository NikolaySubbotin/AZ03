import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка Selenium и запуск браузера
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Запуск в фоновом режиме
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Переход на страницу
    driver.get("https://www.divan.ru/category/pramye-divany")

    # Даем странице загрузиться
    time.sleep(3)

    # Находим элементы, содержащие цены
    prices = driver.find_elements(By.CSS_SELECTOR, "span[data-testid='price']")

    # Открываем файл для записи
    with open('divan_prices.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Price'])  # Записываем заголовок

        # Записываем данные
        for price in prices:
            writer.writerow([price.text])  # Записываем текстовое значение элемента

    print("Данные успешно записаны в divan_prices.csv")

finally:
    # Закрываем браузер
    driver.quit()