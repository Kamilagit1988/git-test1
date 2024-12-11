
import numpy as np

# Создаем массив из списка
array = np.array([1, 2, 3, 4, 5])
print("Массив:", array)
print("Тип данных:", type(array))


# Массив чисел
data = np.array([10, 20, 30, 40, 50])

# Среднее значение
mean_value = np.mean(data)
print("Среднее значение:", mean_value)


# Создаем массив из 5 чисел от 0 до 10
linear_space = np.linspace(0, 10, 5)
print("Равномерно распределенные числа:", linear_space)