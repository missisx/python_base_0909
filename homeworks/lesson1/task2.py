#Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

print ("Введите время в секундах")
time = int(input())

time_sec = time % 60
print(time_sec)
time_min = (time // 60) % 60
print(time_min)
time_hour = (time // 3600)  % 60
print(time_hour)

print(time_hour, time_min, time_sec, sep = ":")