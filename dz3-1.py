import csv
import re

def clean_price(price):
    # Удаляем все символы, кроме цифр, с помощью регулярного выражения
    cleaned_price = re.sub(r'[^\d]', '', price)
    return int(cleaned_price) if cleaned_price else 0


# Чтение данных из исходного CSV файла и их обработка
input_file = 'divan_prices.csv'
output_file = 'cleaned_prices.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='',
                                                                  encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Читаем заголовок и записываем его в новый файл
    header = next(reader)
    writer.writerow(header)

    # Обрабатываем и записываем данные строк
    for row in reader:
        try:
            clean_row = [clean_price(row[0])]
            writer.writerow(clean_row)
        except ValueError as e:
            print(f"Ошибка обработки строки {row}: {e}")

print(f"Обработанные данные сохранены в файл {output_file}")