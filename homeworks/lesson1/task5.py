#Запросите у пользователя значения выручки и издержек фирмы.
#Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
#Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

print("Введите значение выручки фирмы")
proceed = int(input())
print("Введите значение издержек фирмы")
costs = int(input())

if (proceed > costs):
    ratio = proceed / costs
    print ("Фирма отработала с прибылью", ratio)
    print("Введите численность фирмы")
    staff = int(input())
    profit = proceed / staff
    print("Прибыль на одного сотрудника равна", profit)

else:
    print ("Фирма отработала в убыток")