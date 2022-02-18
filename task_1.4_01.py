
# coding: utf-8        # -*- coding: utf-8 -*-

print('\n    Задача 1. Раздел 1.4')
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
print('\n Исходные данные:\n geo_logs = [', end='')
idx = 0
for visit in geo_logs:
    idx += 1
    if idx != 1:
        print(f',\n     {visit}', end='')
    else:
        print(f'\n     {visit}', end='')
print('\n ]')
ru_logs = []
for visit in geo_logs:
    # Получилась очень сложная вложенная структура элемента:
    # visit.values()  ==>  dict_values([['Архангельск', 'Россия']])
    print(f'     {visit}')  #  ==>  dict_values([['Архангельск', 'Россия']])
    print(f'     {visit.values()}')  #  ==>  dict_values([['Архангельск', 'Россия']])
    #print(f'     {list(visit.values())}')  #  ==>  [['Архангельск', 'Россия']]
    #print(f'     {list(visit.values())[0]}')  #  ==>  ['Архангельск', 'Россия']
    #print(f'     {list(visit.values())[0][1]}')  #  ==>  Россия
    #if list(visit.values())[0][1] == 'Россия':
    if 'Россия'in list(visit.values())[0]:
    	# if 'Россия'in visit.values():  -  так не работает ?!?!
        ru_logs.append(visit)
#
#my_str = str(visit.values())
#print(f"\n 'visit.values()': {my_str}")
#
print('\n Вывод:\n ru_logs = [', end='')
idx = 0
for visit in ru_logs:
        idx += 1
        if idx != 1:
            print(f',\n     {visit}', end='')
        else:
            print(f'\n     {visit}', end='')
print('\n ]')

input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
