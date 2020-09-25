# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

users_count = 0
sal = 0
loosers = []
with open('my_task3.txt', 'r', encoding='UTF-8') as my_f:
    for line in my_f:
        users_count += 1
        new_sal = float(line.split(' ')[1])
        sal += new_sal
        if new_sal < 20000:
            loosers.append(line.split(' ')[0])
print(f'Средняя зарплата сотрудников {sal / users_count} руб, оклад менее 20тыс имеют {loosers}')