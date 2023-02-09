# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

list1 = [1, 1, 2, 0, -1, 3, 4, 4 ]
# unic = []
# count = 0
# for element in list1:
#         if element not in unic:
#             unic.append(element)
# print(len(unic))

print(len(set(list1)))