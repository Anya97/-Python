# 1

my_list = [1, {'Alex': 20, 'Sam': 30, 'Max': 5}, 'Hello', 4.5, [True, (1, 2.4, 7), False, False,], 1 + 2j, (1, 3, 9), {1, 8, 5}]

for i in my_list:
    print(type(i))
    
for j in my_list[4]:
    print(type(j))

my_second_list = [ [10, 13, 7j+1, False, 'table'], [1.2, 90, 'cats', 'dogs', 6], [9j+2, 'magic', 99, 13, {'name', 'surname', 'sex'}], [1, 2.3, False, (6, 6, 6), 'true'], ['p', 'o', 'm', 100, 1]]

for l in range(len(my_second_list)):
    for k in range(len(my_second_list[l])):
        print(type(my_second_list[l][k]), end = ' ')
    print()

# 2

lst = [1, 6, 101, 55, 3, 9]

def change_the_list(a):
    for i in range(1, len(a), 2):
        a[i - 1], a[i] = a[i], a[i - 1]
    print(a)

change_the_list(lst)

# 3
# С помощью словаря

month = int(input('Введите месяц от 1 до 12: '))
seasons = {'winter': {12, 1, 2}, 'spring': {3, 4, 5}, 'summer': {6, 7, 8}, 'autumn': {9, 10, 11}}
if month in seasons.get('winter'):
    print('Данный месяц относится к зиме')
elif month in seasons.get('spring'):
    print('Данный месяц относится к весне')
elif month in seasons.get('summer'):
    print('Данный месяц относится к лету')
elif month in seasons.get('autumn'):
    print('Данный месяц относится к осени')
    
#реализация через список, p.s. вышло довольно убого и перебор по всем i, не знаю как этого избежать :(
seasons = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
season = ''
for i in range(len(seasons)):
    for j in range(len(seasons[i])):
        if month == seasons[0][j]:
            season = 'Данный месяц относится к зиме'
        elif month == seasons[1][j]:
            season = 'Данный месяц относится к весне'
        elif month == seasons[2][j]:
            season = 'Данный месяц относится к лету'
        elif month == seasons[3][j]:
            season = 'Данный месяц относится к осени'
print(season)

# 4
# P.S. не очень поняла как пронумеровать не вручную, может быть count()?

my_string = input("Введите строку: ").split()
num = 1
for i in my_string:
    print(f'{num}) {i[:10]}')
    num += 1

#5

rating = [13, 11, 7, 5, 3, 3, 2]
new_element = int(input('Введите новый элемент рейтинга: '))
while True:
    for i, element in enumerate(rating):
        if element == new_element:
            rating.insert(i+1, new_element)
            break
        elif element < new_element:
            rating.insert(i, new_element)
            break
    else:
        rating.append(new_element)
    print(rating)
    new_element = int(input('Введите новый элемент рейтинга: '))

#6

goods = []
while True:
    item_param = input('Введите товар: ').split()
    if len(item_param) == 4:
        item = (len(goods) + 1, {'название': item_param[0], 'цена': item_param[1], 'количество': item_param[2], 'ед': item_param[3]})
        goods.append(item)
        print(goods)
    else:
        print('Некорректный ввод, введите четыре слова')
