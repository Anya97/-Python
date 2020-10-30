#1

import time

class TrafficLight:
    color = 'red'
    
    def running(self):
        if self.color == 'red':
            print('Красный светофор')
            time.sleep(7)
            self.color = 'yellow'
        elif self.color == 'yellow':
            print('Желтный светофор')
            time.sleep(2)
            self.color = 'green'
        elif self.color == 'green':
            print('Зеленый светофор')
            time.sleep(5)
            self.color = 'red'

traffic_light = TrafficLight()

while True:
    traffic_light.running()

#2
class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width
    

    def calculate(self, m = 25, thick = 5):
        return m*self._length*self._width*thick

road1 = Road(55, 35)
road2 = Road(101, 235)
print(road1.calculate())
print(road2.calculate())

#3
class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

position = Position('Serega', 'Pusyk', 'Kotik', 5000, 300)
print(position.get_full_name())
print(position.get_total_income())

#4

class Car:
    speed = int()
    color = ''
    name = ''
    is_police = False
    
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Машина стартовала')
    
    def stop(self):
        print('Машина остановилась')
    
    def turn(self, direction):
        print(f'Машина повернула на {direction}')
    
    def show_speed(self):
        print(f'Скорость автомобиля равна {self.speed} км')

class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            print('Скорость превышена')
        super().show_speed()

class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            print('Скорость превышена')
        super().show_speed()

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.police_car = True

car = Car(30, 'red', 'Lamborghini')
town_car = TownCar(80, 'blue', 'Tayota')
work_car = WorkCar(50, 'black', 'Cat')
police_car = PoliceCar(150, 'purple', 'Dog')
sport_car = SportCar(250, 'white', 'Bugatti')

car.show_speed()
car.go()
car.stop()
car.turn('северо-запад')
work_car.show_speed()
work_car.go()
work_car.stop()
work_car.turn('юго-восток')
town_car.show_speed()
police_car.show_speed()
sport_car.show_speed()

#5
class Stationery:
    title = ''
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self):
        self.title = 'ручка'

    def draw(self):
        print('Пишем ручкой')

class Pencil(Stationery):
    def __init__(self):
        self.title = 'карандаш'

    def draw(self):
        print('Пишем карандашом')

class Handle(Stationery):
    def __init__(self):
        self.title = 'маркер'

    def draw(self):
        print('Пишем маркером')

stationery = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()
stationery.draw()
pen.draw()
pencil.draw()
handle.draw()