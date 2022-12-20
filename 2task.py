# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка

n = int(input("Введите число: "))
def sequence(n):
    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]
print(sequence(n))
print(round(sum(sequence(n))))