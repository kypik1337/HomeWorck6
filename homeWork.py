# оптимизация кода !!! три задачки
#                                                                       Задачка номер 1
                                                                            #было
# num = ( 1,2,3,4,5,6,7)
# day = int(input("add day = "))
# if day <= 5:
#     print("Budnie dni")
# else:
#     print("Gul8nka")
                                                                            # стало
# num = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")
# num_index = ( 1,2,3,4,5,6,7)

# for num_index, num in zip(num_index, num):
#     print(num_index, num)

# day = int(input("add day = "))
# if day <= 5:
#     print(F"будний день пока поработай:= {day}")
# else:
#     print(f"отлично сегодня выходной:= {day}")
                                                                            #стало
# num = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

# for i, num  in enumerate(num):
#     print(i+1,num)

# day = int(input("add day = "))
# if day <= 5:
#     print(F"будний день пока поработай:= {day}")
# else:
#     print(f"отлично сегодня выходной:= {day}")

# и еще к примеру вот такая модернизация через list comprehension
# было
# result_list = []
# for i in new_list:
#     if i % 1 != 0:
#         result_list.append(round(i % 1, 2))
# стало
# result_list = [round(i % 1, 2) for i in new_list if i % 1 != 0]