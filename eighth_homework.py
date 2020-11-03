#1

class Data:
    def __init__(self, data):
        self.data = str(data)
    
    @classmethod
    def my_method(cls, data):
        my_date = []

        for i in str(data).split():
            if i != '-': my_date.append(i)
        
        return int(my_date[0]), int(my_date[1]), int(my_date[2])
    
    @staticmethod
    def my_staticmethod(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 1997:
                    return f'Вы ввели правильную дату'
                else:
                    raise Exception('Вы ввели неправильный год')
            else:
                raise Exception('Вы ввели неправильный месяц')
        else:
            raise Exception('Вы ввели неправильный день')
    
    def __str__(self):
        return f'Текущая дата {Data.my_method(self.data)}'
    
today = Data('11 - 1 - 2001')
print(Data.my_method('23 - 3 - 1997'))
print(today.my_method('23 - 3 - 2001'))
print(today.my_staticmethod(23, 3, 1997))
print(Data.my_staticmethod(23, 3, 2000001))

#2
class MyException:
#    def __init__(self, param_1, param_2):
#        self.param_1 = param_1
#        self.param_2 = param_2
    
    @staticmethod
    def my_div(param_1, param_2):
        try:
            return param_1 / param_2
        except ZeroDivisionError:
            print("Деление на ноль недопустимо")

my_except = MyException()
print(MyException.my_div(10, 4))
my_except.my_div(10, 0)

#3
class MyException:
    numbers_list = []

    def fill_list(self):
        while True:
            try:
                a = input('Введите число: ')
                self.numbers_list.append(int(a))
                print(self.numbers_list)
            except ValueError:
                if a == 'stop':
                    break
                else:
                    print('Вы ввели фигню')

my_exception = MyException()
my_exception.fill_list()

#4
class Warehouse:
    pass
class OfficeEquipment:
    def __init__(self, number, size, quality):
        self.number = number
        self.size = size
        self.quality = quality

class Printer(OfficeEquipment):
    def number_of_pages(self, number):
        self.number = number

class Scanner(OfficeEquipment):
    def scanning_speed(self, speed):
        self.speed = speed

class Xerox(OfficeEquipment):
    def field_of_application(self, application):
        self.application = application

#5

class Warehouse:
    def __init__(self, equipments):
        self.equipments = equipments
        print(equipments)

#class OfficeEquipment(Warehouse):
#    def __init__(self, number, size, quality):
#        self.number = number
#        self.size = size
#        self.quality = quality

class Printer(Warehouse):
    def number_of_pages(self, number):
        self.number = number

    def my_printer(self):   
        for key, value in self.equipments.items():
            if 'printer' in self.equipments:
                if key == 'printer':
                    print('принтеры есть в наличии')
                    print(f'{key} : {value} шт')
            else:
                print('принтеров нет в наличии')
        

class Scanner(Warehouse):
    def scanning_speed(self, speed):
        self.speed = speed
    
    def my_scanner(self):   
        for key, value in self.equipments.items():
            if 'scanner' in self.equipments:
                if key == 'scanner':
                    print('сканеры есть в наличии')
                    print(f'{key} : {value} шт')
            else:
                print('сканеров нет в наличии')

class Xerox(Warehouse):
    def field_of_application(self, application):
        self.application = application
    
    def my_xerox(self):   
        for key, value in self.equipments.items():
            if 'xerox' in self.equipments:
                if key == 'xerox':
                    print('ксероксы есть в наличии')
                    print(f'{key} : {value} шт')
            else:
                print('ксероксов нет в наличии')

#warehouse = Warehouse({'printer': 26, 'scanner': 15, 'xerox': 90})
#warehouse.__init__({'printer': 26, 'scanner': 15, 'xerox': 90})
printer = Printer({'printer': 26, 'scanner': 15, 'xerox': 90})
printer.my_printer()
scanner = Scanner({'printer': 26, 'scanner': 15, 'xerox': 90})
scanner.my_scanner()
xerox = Xerox({'printer': 26, 'scanner': 15, 'xerox': 90})
xerox.my_xerox()

#6
class Warehouse:
    def __init__(self, equipments):
        self.equipments = equipments
        print(equipments)

#class OfficeEquipment(Warehouse):
#    def __init__(self, number, size, quality):
#        self.number = number
#        self.size = size
#        self.quality = quality

class Printer(Warehouse):
    def number_of_pages(self, number):
        self.number = number

    def my_printer(self):   
        for key, value in self.equipments.items():
            if 'printer' in self.equipments:
                if key == 'printer':
                    print('принтеры есть в наличии')
                    print(int(value))
            else:
                print('принтеров нет в наличии')
        

class Scanner(Warehouse):
    def scanning_speed(self, speed):
        self.speed = speed
    
    def my_scanner(self):   
        for key, value in self.equipments.items():
            if 'scanner' in self.equipments:
                if key == 'scanner':
                    print('сканеры есть в наличии')
                    print(int(value))
            else:
                print('сканеров нет в наличии')

class Xerox(Warehouse):
    def field_of_application(self, application):
        self.application = application
    
    def my_xerox(self):   
        for key, value in self.equipments.items():
            if 'xerox' in self.equipments:
                if key == 'xerox':
                    print('ксероксы есть в наличии')
                    print(int(value))
            else:
                print('ксероксов нет в наличии')

#warehouse = Warehouse({'printer': 26, 'scanner': 15, 'xerox': 90})
#warehouse.__init__({'printer': 26, 'scanner': 15, 'xerox': 90})
printer = Printer({'printer': 26, 'scanner': 15, 'xerox': 90})
printer.my_printer()
scanner = Scanner({'printer': 26, 'scanner': 15, 'xerox': 90})
scanner.my_scanner()
xerox = Xerox({'printer': 26, 'scanner': 15, 'xerox': 90})
xerox.my_xerox()

#7
class ComplexNumbers:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return ComplexNumbers(self.num_1 + other.num_1, self.num_2 + other.num_2)

    def __mul__(self, other):
        return ComplexNumbers(self.num_1 * other.num_1, self.num_2 * other.num_2)

    def __str__(self):
        return f'результат: {self.num_1} , {self.num_2}'

x = complex(3, 4)
y = complex(7, 8)
z = complex(-1, 5)
q = complex(2, 1)
a = ComplexNumbers(x, y)
b = ComplexNumbers(z, q)
print(a+b)
print(a*b)