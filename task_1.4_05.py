
# coding: utf-8        # -*- coding: utf-8 -*-

print('\n    Задача 5. Раздел 1.4\n')
source_ls = ['2018-01-01', 'yandex', 'cpc', 100]
print(f'\n Исходные данные:\n source_ls: {source_ls}')
print('\n Вывод:')
if len(source_ls) >= 2:
    my_val = source_ls[-1]
    for my_key in source_ls[-2::-1]:
        my_dict = {my_key: my_val,}
        my_val = my_dict
    print(f' my_dict:   {my_dict}')
else:
    print('\n В заданном списке меньше двух элементов.\n Словарь создать невозможно')

input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды

# 9643100203317290945 - моя
# 9643100203312504647 - Эльвирина