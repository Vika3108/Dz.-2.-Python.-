# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int

import random
list = [random.randint(0, 10) for i in range(random.randint(5,20))]
print(f"Исходный список: \n {list}")
random.shuffle(list)
print(f"Список после перемешивания: \n{list}")