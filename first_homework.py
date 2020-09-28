# 1

a = int(input('Введите целое число: '))
print(a)

b = input('Введите слово: ')
print(b)

c = input('Введите числа или буквы: ').split()
print(c)

d = [int(i) for i in input().split()]
print(d)

#2

sec = int(input('Введите время в секундах: '))
hours = sec//3600
minutes = (sec//60)%60
seconds = sec%60

print(f'{hours}:{minutes}:{seconds}')


#3

n = int(input('Введите число: '))
print(n+int(2*str(n))+int(3*str(n)))

#4
n = input('Введите целое положительное число: ').split()
for i in n:
    print(max(i))

#5

a = int(input('Введите выручку фирмы: '))
b = int(input('Введите издержки фирмы: '))
print(f'Выручка вашей фирмы:{a}, издержки вашей фирмы:{b}')
if a>b:
    print(f'Рентабельность прибыли:{(a-b)/a}')
    workers = int(input('Введите число сотрудников фирмы: '))
    print(f'Прибыль на одного сотрудника в фирме:{(a-b)/workers}')

else:
    print('Фирма не отработала с прибылью')

#6

a = int(input('Введите сколько километров пробежал спортсмен в первый день: '))
b = int(input('Введите ожидаемые результаты: '))
c = 1
d = a
print('Результат:')
while d<b:
    print(f'{c}-й день: {round(d, 2)}')
    d += 0.1*a
    c += 1
else:
    print(f'{c}-й день: {round(d+0.1*d, 2)}')
    print(f'Ответ: на {c}-й день спортсмен достиг результата — не менее {b} км')
