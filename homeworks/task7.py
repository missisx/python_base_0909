# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

my_file = open("my-task7.txt", "w", encoding='UTF-8')
my_file.writelines(['firm_1 ООО 10000 500\n', 'firm_2 ООО 100 500\n', 'firm_3 ИП 500 500\n'])
my_file.close()

my_dict = {}
my_list = []
my_file = open("my-task7.txt", "r", encoding='UTF-8')
sum, count = 0, 0
for line in my_file:
    tmp = line.split(' ')
    profit = int(tmp[2])
    lost = int(tmp[3])
    my_dict.update({tmp[0]: profit - lost})
    count += 1
    if (profit - lost) > 0:
        sum += profit - lost
my_list.append(my_dict)
my_list.append({"average_profit": sum / count})

with open("my_file7.json", "w", encoding='UTF-8') as write_f:
    json.dump(my_list, write_f)