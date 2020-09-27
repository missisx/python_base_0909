# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed = 0.0
    color = ''
    name =''
    is_police = False

    def __init__(self, us_speed, us_name, us_color):
        self.speed = us_speed
        self.color = us_color
        self.name = us_name

    def go(self):
        self.speed = 40.0
        print(f'Автомобиль {self.name} движется\n')
    def stop(self):
        self.speed = 0.0
        print(f'Автомобиль {self.name} остановился\n')
    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул {direction}\n')
    def showSpeed(self):
        print(f'Текущая скорость автомобиля {self.name} составляет {self.speed} км/ч\n')

class TownCar(Car):
    def showSpeed(self):
        if self.speed > 60:
            print(f'Автомобиль {self.name} превышает скорость, его скорость {self.speed} км/ч\n')
        else:
            print(f'Текущая скорость автомобиля {self.name} составляет {self.speed} км/ч\n')

class SportCar(Car):
    def is_on_competition(self):
        print(f'Автомобиль {self.name} участвует в гонках\n')

class WorkCar(Car):
    def showSpeed(self):
        if self.speed > 40:
            print(f'Автомобиль {self.name} превышает скорость, его скорость {self.speed} км/ч\n')
        else:
            print(f'Текущая скорость автомобиля {self.name} составляет {self.speed} км/ч\n')

class PoliceCar(Car):
    is_police = True

car1 = PoliceCar(50.0, "Полиция", "черный")
car2 = WorkCar(20.0, "Рабочая машина", "белый")
car3 = WorkCar(100.0, "Рабочая экстренная", "красный")
car4 = SportCar(50.0, "Спортивная", "серый")
car5 = TownCar(62.0, "Городская", "синий")
car1.showSpeed()
car2.showSpeed()
car3.showSpeed()
car4.showSpeed()
car5.showSpeed()
car1.go()
car1.turn("налево")
car1.go()
car1.turn("направо")
car1.stop()
print(f'Цвет автомобиля {car1.color}')