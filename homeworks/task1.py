# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

var_list = [0, True, 1.33, 'a', "Omsk", (1, 2), [3, 4], None]
for item in var_list:
   if (type(item)==int):
       print("Целое число")
   elif (type(item) == float):
       print("С плавающей точкой")
   elif (type(item) == str):
       print("Строка")
   elif (type(item)==list):
       print("Список")
   elif (type(item)==tuple):
       print("Кортеж")
   elif (type(item)==bool):
       print("Булевый тип")
   else:
       print(type(item))