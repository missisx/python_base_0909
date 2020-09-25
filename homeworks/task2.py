# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_file = open("my_task2.txt", 'r')
num_str = 0
for line in my_file:
    num_str += 1
    num_word = line.count(' ') + 1 if not line == '\n' else 0
    print(f'Строка {num_str} содержит {num_word} слов')
my_file.close()