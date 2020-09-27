# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name =''
    surname = ''
    position=''
    _income = {"wage": 0.0, "bonus": 0.0}

    def __init__(self, us_surname, us_name, us_position ):
        self.name = us_name
        self.surname = us_surname
        self.position = us_position

    def set_income(self, us_wage, us_bonus):
        self._income.update({"wage": float(us_wage), "bonus": float(us_bonus)})

class Position (Worker):

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return super()._income.get("wage") + super()._income.get("bonus")

position1 = Position('Иванов', 'Иван', 'менеджер')
position1.set_income(1000, 500)
print(f'Сотрудник {position1.get_full_name()} получает {position1.get_total_income()} руб')
