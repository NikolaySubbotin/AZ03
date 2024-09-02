import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(5)
y = np.random.rand(5)

print(f"массив из 5 случайных чисел x - {x}")
print(f"массив из 5 случайных чисел y - {y}")

plt.scatter(x, y)

plt.xlabel('ось х')
plt.ylabel('ось у')
plt.title('Диаграмма рассеяния для двух наборов')

plt.show()