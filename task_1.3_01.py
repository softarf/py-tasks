
# coding: utf-8        # -*- coding: utf-8 -*-

print('\n    Задача 1. Раздел 1.3')
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) == len(girls):
    print('\n Идеальные пары:')
    '''
    # Универсальный вариант: список pair[] удобен для переменного числа аргументов функции zip
    for pair in zip(sorted(boys), sorted(girls)):
        print(f' {pair[0]} и {pair[1]}')
    '''
    #   Альтернативный вариант: список pair[] распакован на две переменные boy и girl,
    #   соответственно, для двух аргументов функции zip.
    #   Запись с явным указанием элементов Понятнее, поэтому Приветствуется.
    for boy, girl in zip(sorted(boys), sorted(girls)):
        print(f' {boy} и {girl}')
else:
    print('\n Кто-то может остаться без пары!')

input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
