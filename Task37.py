# Задача №37. Решение в группах
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def revert(n):
    if n == 0:
        return " "
    k = int(input("Enter element: "))
    return revert(n-1) + f"{', 'if n > l else ''} {k} "

l = int(input("Enter number: "))
print(revert(l))