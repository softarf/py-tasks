
# Учебный файл по лекции 4

ls1 = [['Дели', 'Мумбаи'], ['Москва', 'Нефтекамск'],['Лиссабон', 'Порту'], 'Париж', ['Берлин', 'Мюнхен']]
ls2 = ['Индия', 'Россия', 'Португалия', 'Франция', 'Германия']
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
          # Ещё можно и так. Который список короче, столько элементов получится.
my_dict2 = dict(zip(ls2, ls1[:4]))
print(f' my_dict2: {my_dict2}')
print('\n            Работа с ключами')
# capital country
# country = 'Украина'
# country = 'Германия'
country = 'Россия'
if country in my_dict.keys():  # Проверка ключа на присутствие
	print(f'\n Страна {country} есть')
else:
	print(f'\n Страны {country} нет')
country = 'Украина'
if country in my_dict.keys():  # Проверка ключа на присутствие
	print(f'\n Страна {country} есть')
else:
	print(f'\n Страны {country} нет')
country = 'Германия'
if country in my_dict.keys():  # Проверка ключа на присутствие
	print(f'\n Страна {country} есть')
else:
	print(f'\n Страны {country} нет')
print(f'\n Добавляем {country}')
my_dict[ls2[4]] = ls1[4]
if country in my_dict.keys():  # Проверка ключа на присутствие
	print(f'\n Страна {country} есть')
else:
	print(f'\n Страны {country} нет')
print(f'\n my_dict: {my_dict}')
country = 'Индия'
print(f'\n Удаляем {country}')
del(my_dict[country])
print(f'\n my_dict: {my_dict}\n')
print('\n            Работа с записями\n')
for item in my_dict2.items():
		print(f' my_dict2.items(i): {item}')
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
print(f' my_dict2.values(): {my_dict2.values()}')
print(f" my_dict2['Индия']: {my_dict2['Индия']}")
