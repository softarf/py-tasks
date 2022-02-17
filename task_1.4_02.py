
# coding: utf-8        # -*- coding: utf-8 -*-

print('\n    Задача 2. Раздел 1.4')
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
print('\n Исходные данные:\n ids = {', end='')
idx = 0
for user_name, user_id in ids.items():
    idx += 1
    if idx != 1:
        print(f",\n        '{user_name}': {user_id}", end='')
    else:
        print(f"'{user_name}': {user_id}", end='')
print('}')

all_ids_1 = []
print(f'\n all_ids_1: {all_ids_1}')  # Для теста
all_ids_2 = []
print(f' all_ids_2: {all_ids_2}')  # Для теста
for key in ids.keys():
    all_ids_1.extend(ids[key])
    print(f' key: {key}    ids[key]: {ids[key]}  \tall_ids_1: {all_ids_1}')  # Для теста
    all_ids_2 += ids[key]
    print(f' key: {key}    ids[key]: {ids[key]}  \tall_ids_2: {all_ids_2}')  # Для теста
#
all_ids_set = set(all_ids_1)
#
print(f'\n all_ids_set: {all_ids_set}')  # Для теста
#
geo_ids = list(all_ids_set)
print(f'\n Вывод:\n geo_ids = {geo_ids}')

input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
