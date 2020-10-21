#1

def division():
    try:
        arg_1 = float(input('Введите первое число: '))
        arg_2 = float(input('Введите второе число: '))
        return arg_1 / arg_2
    except ZeroDivisionError:
        print('Деление на ноль')
res = division()
print(res)

# 2

def person():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    year = int(input('Введите год рождения: '))
    city = input('Введите город проживания: ')
    email = input('Введите email: ')
    number = int(input('Введите номер телефона: '))
    print(f'имя: {name}, фамилия: {surname}, год рождения: {year}, город проживания: {city}, email: {email}, телефон {number}') 
person()

# 3

def my_funk(arg_1, arg_2, arg_3):
    return max((arg_1 + arg_2, arg_1 + arg_3, arg_2 + arg_3))
res = my_funk(11, 5, 9000)
print(res)

# 4
# 1 сп-б
def my_funk(x, y):
    return x ** y
res = my_funk(5, -1)
print(res)

# 2 сп-б
def my_funk(x, y):
    counter = 1
    result = 1
    while counter <= abs(y):
        result /= x
        counter += 1
    return result
res = my_funk(5, -4)
print(res)

# 5
def sum():
    count = 0
    while True:
        numbers = input('Введите числа через пробел: ').split()
        try:
            for i in numbers:
                count += int(i)
            print(count)
        except ValueError:
                break
sum()


# 6

def int_func():
    words = input('Введите несколько слов через пробел: ').split()
    wrd = ''
    for i in words:
        result = str(i.title())
        wrd += result + ' '
    return wrd

res = int_func()
print(res)

