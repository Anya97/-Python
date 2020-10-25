#1

with open('text.txt', 'w') as f_obj:
    my_var = input('Введите строчку: ')
    while my_var != ' ':
        f_obj.write(my_var + '\n')
        my_var = input('Введите строчку: ')

#2
f = open ('my_file.txt', 'r+')
f.write('Добро пожаловать в файл' + '\n' + 'Данный файл предназначен для частного пользования' + '\n' + 'Пока-пока')
count = 0
for index, value in enumerate(f):
    number_of_words = len(value.split())
    count += 1
    print(f'В {count} строке {number_of_words} слов(а)')
f.close()

#3
names = input('Введите фамилию сотрудников: ').split()
salary = input('Введите оклад сотрудников: ').split()
with open('workers.txt', 'r+') as f:
    my_dict = {k:v for k,v in zip(names, salary)}  
    money = 0
    for key, value in my_dict.items():
        f.write(key + ': ' + value + '\n')
        money += int(value)
        if int(value) < 20000:
            print(f'Данный сотрудник имеет оклад менее 20тыс.: {key}')
    num = len(my_dict.keys())
    print(f'Средняя величина дохода сотрудников: {money/num}')

#4
with open('numbers.txt', 'r') as f_obj:
    for line in f_obj:
        eng_num = line.split()
        if eng_num[0] == 'One':
            eng_num[0] = 'Один'
            eng_num_res = ' '.join(eng_num)
        elif eng_num[0] == 'Two':
            eng_num[0] = 'Два'
            eng_num_res = ' '.join(eng_num)
        elif eng_num[0] == 'Three':
            eng_num[0] = 'Три'
            eng_num_res = ' '.join(eng_num)
        elif eng_num[0] == 'Four':
            eng_num[0] = 'Четыре'
            eng_num_res = ' '.join(eng_num)
        with open('russ_numbers.txt', 'a') as f:
            f.write(eng_num_res + '\n')

#5
with open ('sum.txt', 'x') as f_obj:
    numbers = input('Введите набор чисел через пробел: ').split()
    sum = 0
    for i in numbers:
        sum += int(i)
        f_obj.write(str(i) + ';')
    f_obj.write(f' Сумма всех чисел: {sum}')
    print(f'Сумма всех чисел: {sum}')
#6
import re
with open ('lessons.txt') as f_obj:
    less = []
    nums_res = []
    k = 0
    for line in f_obj:
        nums = [int(s) for s in line.split() if s.isdigit()]
        for j in nums:
            k += j
        nums_res.append(k)
        k = 0
        my_str = re.sub(r'[.:()—]', '', line)
        res = my_str.split()
        less.append(res[0])
    my_dict = {k:v for k,v in zip(less, nums_res)}  
    print(my_dict)

#7
with open('firms.txt', 'r') as f_obj:
    firms = []
    profit = []
    loss = []
    firm_with_loss = []
    prf = 0
    frms = 0
    for line in f_obj:
        my_lst = line.split()
        firm_profit = int(my_lst[2]) - int(my_lst[3])
        if firm_profit > 0:
            prf += firm_profit
            frms += 1
            average = prf/frms
            average_profit_dict = {'average_profit':''}
            firms.append(my_lst[0])
            profit.append(firm_profit)
            my_dict_profit = {k:v for k,v in zip(firms, profit)}
        else:
            firm_with_loss.append(my_lst[0])
            loss.append(firm_profit)
            my_dict_loss = {k:v for k,v in zip(firm_with_loss, loss)}
        
    average_profit_dict ['average_profit'] = int(average)

data = [my_dict_profit, my_dict_loss, average_profit_dict]
print(data)
import json
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)    
        




    