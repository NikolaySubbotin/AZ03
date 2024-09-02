# Создай гистограмму для случайных данных,
# сгенерированных с помощью функции `numpy.random.normal`.
# # Параметры нормального распределения
# mean = 0       # Среднее значение
# std_dev = 1    # Стандартное отклонение
# num_samples = 1000  # Количество образцов
# # Генерация случайных чисел, распределенных по нормальному распределению
# data = np.random.normal(mean, std_dev, num_samples)

import numpy as np
import matplotlib.pyplot as plt

mean = 0
std_dev = 1
num_samples = 1000

data = np.random.normal(mean, std_dev, num_samples)

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30,)
plt.title('Гистограмма для случайных данных')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)
plt.show()