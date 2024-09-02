import csv
import matplotlib.pyplot as plt

# Чтение данных из файла cleaned_prices.csv
prices = []

with open('cleaned_prices.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Пропуск заголовка
    next(reader)

    # Чтение цен и преобразование их в целые числа
    for row in reader:
        prices.append(int(row[0]))

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=10, edgecolor='black', color='skyblue')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Количество товаров')
plt.grid(True)

# Сохранение графика в файл и отображение
plt.savefig('price_histogram.png')
plt.show()