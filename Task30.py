# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и 
# количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

n = int(input('Enter n '))
a = [0]*n
a[0] = int(input('Enter a '))
d = int(input('Enter d '))
print(a[0],end=' ')
for i in range(1,n):
    a[i]= a[i-1]+d
    print(a[i],end=' ')



# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
#     print(a1 + i * d)
