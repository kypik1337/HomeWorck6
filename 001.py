# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# *Пример:*

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# out_list =[]

# for i in range(len(my_list)):
#     if my_list.count(my_list[i]) == 1:
#         out_list.append(my_list[i])
# print(out_list)
# # через словарь мочим 

# my_lov = {}

# my_lov = set(my_list)
# my_list_null = [0,0,0,0,0]
# my_lov2 = dict(zip(my_lov,my_list_null))
# for i in my_list:
#     my_lov2[i] += 1
# out_list_2 = []
# for i in my_lov2.keys():
#     if my_lov2.get(i) == 1:
#         out_list_2.append(i)
# print (out_list_2)


#                                                              вторая задачка )                 codewars

# 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:*

# 2+2 => 4;

# 1+2*3 => 7;

# 1-2*3 => -5;


