#Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
import random

def my_more(num: tuple)->list:
    a = num[0]
    new_numbers = []
    for itm in num:
        if itm > a:
            new_numbers.append(itm)
        a = itm
    return new_numbers

'''
user_list = input("Введите набор чисел\n").split()
print(user_list)
try:
    user_numbers = [int(itm) for itm in user_list]
    print(user_numbers)
except ValueError:
    "Введите числа, обнаружено неверное значение"
'''
user_numbers = []
for _ in range(10):
    user_numbers.append(random.randint(0, 115))
print(user_numbers)
print(my_more(user_numbers))