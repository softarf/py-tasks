
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
print()  # Для теста
all_ids_list = []
for key in ids.keys():
    print(f' {ids[key]}')  # Для теста
    all_ids_list.extend(ids[key])
#
print(f' all_ids: {all_ids_list}')  # Для теста
#
all_ids_set = set(all_ids_list)
geo_ids = list(all_ids_set)
print(f'\n Вывод:\n geo_ids = {geo_ids}')

input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
