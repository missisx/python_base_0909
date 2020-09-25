# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import functools

my_file = open('my-task5.txt', 'x', encoding='UTF-8')
my_file.write('6')
for i in range(10):
    my_file.write(' ' + str(i))
with open('my-task5.txt', 'r', encoding='UTF-8') as my_file:
    s = my_file.readline().split(' ')
a = functools.reduce(lambda x, y: int(x) + int(y), s)

print(f'Сумма чисел в файле равна {a}')
my_file.close()