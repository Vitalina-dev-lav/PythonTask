# Задача №33. Общее обсуждение
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

n = int(input('Введите количество оценок: '))

grades=[0]*n

for i in range(n):
    grades[i] = int(input('Введите оценку:'))
maxi_num=max(grades)
mini_num=min(grades)

for i in range(n):
    if grades[i] ==maxi_num:
        grades[i]=mini_num

print(grades)