
# Учебный файл по лекции 4

def ins_key(some_dict, some_country):  # Проверка ключа на присутствие
	if some_country in some_dict.keys():
		print(f'\n Страна {some_country} есть')
	else:
		print(f'\n Страны {some_country} нет')

ls1 = [['Дели', 'Мумбаи'], ['Москва', 'Нефтекамск'],['Лиссабон', 'Порту'], 'Париж', ['Берлин', 'Мюнхен']]
ls2 = ['Индия', 'Россия', 'Португалия', 'Франция', 'Германия']
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit10': ['Архангельск', 'Россия']}
]
print()
for index in ls1:
	print(index, end='\t')
print()
for index in ls2:
	print(index, end='\t')
print()
								# Создаём пустой словарь
my_dict = {}
my_dict2 = dict()
for i in range(3):              # Наполняем словарь из двух списков:
	my_dict[ls2[i]] = ls1[i]    # ls2 список ключей, ls1 список значений.
print(f'\n my_dict: {my_dict}')
print(f' my_dict.values(): {my_dict.values()}\n')
          # Ещё можно и так. Который список короче, столько элементов получится.
my_dict2 = dict(zip(ls2, ls1[:4]))
print(f' my_dict2: {my_dict2}')
print('\n            Работа с ключами')
# capital country
# country = 'Украина'
# country = 'Германия'
country = 'Россия'
ins_key(my_dict, country)  # Проверка ключа на присутствие
country = 'Украина'
ins_key(my_dict, country)  # Проверка ключа на присутствие
country = 'Германия'
ins_key(my_dict, country)  # Проверка ключа на присутствие
print(f'\n Добавляем {country}')
my_dict[ls2[4]] = ls1[4]   # Добавляем Францию
ins_key(my_dict, country)  # Проверка ключа на присутствие
print(f'\n my_dict: {my_dict}')
country = 'Индия'
print(f'\n Удаляем {country}')
del(my_dict[country])
print(f'\n my_dict: {my_dict}\n')
print('\n            Работа с записями\n')
for item in my_dict2.items():
		print(f' my_dict2.items(i): {item}')
print(f' type(my_dict2.items()): {type(my_dict2.items())}')
print(f' my_dict2.items(): {my_dict2.items()}')
item = ('Индия', ['Дели', 'Мумбаи'])
if item in my_dict2.items():  # Проверка записи на присутствие
	print(f'\n Запись {item} есть')
else:
	print(f'\n Записи {item} нет')
print('\n            Работа со значениями\n')
for val in my_dict2.values():
		print(f' my_dict2.values(i): {val}')
val = ['Дели', 'Мумбаи']
if val in my_dict2.values():  # Проверка значения на присутствие
	print(f'\n Запись {val} есть')
else:
	print(f'\n Записи {val} нет')
print()
val = ['Владимир', 'Россия']
for visit in geo_logs:
    # print(f' visit: {visit}')           #  ==>  {'visit1': ['Москва', 'Россия']}
    for vis in visit.values():    # После присваивания всё лишнее отбрасывается, получим чистое значение.
    	print(f' vis: {vis}')
    	# print(f' visit.values(): {visit.values()}')
print(f'\n type(visit): {type(visit)}')
print(f' type(visit.keys()): {type(visit.keys())}')
print(f' type(visit.values()): {type(visit.values())}')
print(f' type(visit.items()): {type(visit.items())}')
print(f' visit.values(): {visit.values()}')
print(f'\n type(vis): {type(vis)}')
print(f'\n my_dict2.values(): {my_dict2.values()}')
print(f" my_dict2['Индия']: {my_dict2['Индия']}")

# print('\n  -- Конец --  ')  #                 - Для блокнота
input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
