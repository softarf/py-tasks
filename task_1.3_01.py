
# coding: utf-8        # -*- coding: utf-8 -*-

print('\n    Задача 1. Раздел 1.3')
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) == len(girls):
    print('\n Идеальные пары:')
    for pair in zip(sorted(boys), sorted(girls)):
        print(f' {pair[0]} и {pair[1]}')
else:
    print('\n Кто-то может остаться без пары!')

input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
