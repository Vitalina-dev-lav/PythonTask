# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:300  Вывод:220 284

k=int(input("Введите число K: "))
my_list=[]
for i in range(k):
    sum_i=0
    for j in range(1, i//2+1):
        if i%j==0:
            sum_i+=j
    my_list.append((i, sum_i))

for i in range(len(my_list)-1):
    for j in range(i+1,len(my_list)):
        if my_list[i][0]==my_list[j][1] and my_list[j][0]==my_list[i][1]:
            print(*my_list[i])