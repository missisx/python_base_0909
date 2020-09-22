#Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
#Результат: [23, 1, 3, 10, 4, 11]
import random

def my_f(nums: list) -> list:
    us_set = set(nums)
    new_nums = []
    for item in us_set:
        if nums.count(item) == 1:
            new_nums.append(item)
    return new_nums

#user_nums = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
user_nums = []
for itm in range(10):
    user_nums.append(random.randint(0, 25))
uniq = my_f(user_nums)
result =[]
for item in user_nums:
    if item in uniq:
        result.append(item)
print(result)