# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

def my_isfloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def my_salary (hs: float, perh: float, pr: float) -> float:
    return  (hs * perh) + pr

while True:
    a = input("Введите выработку в часах для сотрудника\n")
    if my_isfloat(a):
        a = float(a)
        break

while True:
    b = float(input("Введите ставку в час для сотрудника\n"))
    if my_isfloat(b):
        b = float(b)
        break

while True:
    c = input("Введите премию для сотрудника\n")
    if my_isfloat(c):
        c = float(c)
        break

print(my_salary(a, b, c))

