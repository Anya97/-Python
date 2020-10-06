# 1

from sys import argv  

def employee_salary(argv):
    try:
        salary = (int(argv[1]) * int(argv[2])) + int(argv[3])
        print(salary)
    except IndexError:
        print('Введите количество отработанных часов, ставку в час и премию')
employee_salary(argv)

#2


def list_to_list(list_1):
    list_2 = [list_1[i] for i in range(1, len(list_1)) if list_1[i] > list_1 [i - 1]]
    return list_2
list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = list_to_list(list_1)
print(result)

#3
my_list = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]


#4
my_first_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_second_list = [i for i in my_first_list if my_first_list.count(i) == 1]
print(my_second_list)


#5
def num_gen():
    res = 1
    first_lst = [int(i) for i in range(100, 1001) if i%2 == 0]
    for i in first_lst:
        res *= i
    return res
    

num_result = num_gen()
print(num_result)

#6 (а)
from itertools import count

for i in count(3):
    if i > 10:
        break
    else:
        print(i)

#6 (б)
from itertools import cycle

num = 0
for i in cycle([11, 1, 2, 8, 3, 55]):
    if num > 20:
        break
    print(i)
    num += 1

#7
def fact(n):
    a, b = 1, 1

    while a <= n:
        b *= a
        yield b
        a += 1

fact_gen = fact(10)       
for i in fact(10):
    print(i)
