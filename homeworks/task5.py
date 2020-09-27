#  Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
#  (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
#  Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
#  Для каждого из классов методы должен выводить уникальное сообщение.
#  Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = ''

    def __init__(self, us_title):
        self.title = us_title

    def draw(self):
        print('Запуск отрисовки\n')

class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой\n')

class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером\n')

class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом\n')

pen1 = Pen('ручка')
pen1.draw()
pencil1 = Pencil('карандаш')
pencil1.draw()
handle1 = Handle('маркер')
handle1.draw()
paint1 = Stationery('краска')
paint1.draw()
