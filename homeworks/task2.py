# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list=[]
print("Введите значения списка")
while True:
    a=input()
    if (len(a)):
        list.append(a)
    else:
        break

print(list)
print(len(list) // 2)

for idx in range( len(list) // 2):
    a = list[idx*2]
    list[idx*2] = list[idx*2+1]
    list[idx*2+1] = a

print(list)