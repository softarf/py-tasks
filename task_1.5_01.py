
# coding: utf-8        # -*- coding: utf-8 -*-

'''
19.01.22
Не успел реализовать функции "Перенос документа на другую полку"
и "Создание новой полки".
Может к окончанию проверки успею.
20.01.22
Добавил функции "Перенос документа на другую полку"
и "Создание новой полки".
'''
def print_docs(my_docs):
    print(' Документы: documents = [', end='')
    idx = 0
    for document in my_docs:
        idx += 1
        if idx != 1:
            print(f',\n     {document}', end='')
        else:
            print(f'\n     {document}', end='')
    print('\n    ]')
    return

def print_dirs(my_dirs):
	print(' Полки: directories = {', end='')
	idx = 0
	for dir_num, dir_content in my_dirs.items():
		idx += 1
		if idx != 1:
			print(f",\n     '{dir_num}': {dir_content}", end='')
		else:
			print(f"\n     '{dir_num}': {dir_content}", end='')
	print('\n    }')
	return

def desiring_person(my_docs):
	indicate = True
	num_doc = input('\n Введите номер документа: ')
	for document in my_docs:
		if num_doc == document["number"]:
			indicate = False
			print(' Искомый name:', document["name"])
			break
	if indicate:
		print(f"\n Нет документа с номером '{num_doc}'")
	# print_docs(my_docs)  # Для теста
	return
	
def desiring_shelf(my_dirs):
	indicate = True
	num_doc = input('\n Введите номер документа: ')
	for num_shelf in my_dirs.keys():
		if num_doc in my_dirs[num_shelf]:
			indicate = False
			print(f" Искомая полка: '{num_shelf}'")
			break
	if indicate:
		print(f"\n Нет документа с номером '{num_doc}'")
	# print_dirs(my_dirs)  # Для теста
	return
		
def listing_docs(my_docs):
	print('\n Имеются документы:\n')
	for document in my_docs:
		idx = 0
		for key in document.keys():
			idx += 1
			if idx != 1:
				print(f' "{document[key]}" ', end=' ')
			else:
				print(f' {document[key]} ', end=' ')
		print()
	# print_docs(my_docs)  # Для теста
	return
		
def create_new_doc(my_docs, my_dirs):
	ind_quite = True
	print('\n Создание нового документа (q - отмена).')
	my_type = input(' Введите тип документа: ')
	if my_type.strip().lower() != 'q':
		my_num = input(' Введите номер документа: ')
		if my_num.strip().lower() != 'q':
			my_name = input(' Введите имя: ')
			if my_name.strip().lower() != 'q':
				bool_while = True
				while bool_while:
					my_shelf = input(' Введите номер полки: ')
					if my_shelf.strip().lower() != 'q':
						if my_shelf in my_dirs.keys():
							new_doc = {"type": my_type, "number": my_num, "name": my_name}
							my_docs.append(new_doc)
							my_dirs[my_shelf].append(new_doc["number"])
							print('\n Запись добавлена')
							ind_quite = False
							bool_while = False
						else:
							print('\n Нет такой полки')
					else:
						bool_while = False
	if ind_quite:
		print('\n Операция отменена')
	# print_docs(my_docs)  # Для теста
	# print_dirs(my_dirs)  # Для теста
	return
			
def delete_doc(my_docs, my_dirs):
	print('\n Удаление старого документа (q - отмена).')
	while_num = True
	while while_num:
		my_num = input(' Введите номер документа: ')
		if my_num.strip().lower() != 'q':
			indicate = True
			for idx, doc in enumerate(my_docs):
				if my_num == doc["number"]:
					del my_docs[idx]
					for key in my_dirs:
						if my_num in my_dirs[key]:
							my_dirs[key].remove(my_num)
							break
					print(f"\n Документ '{my_num}' удалён")
					indicate = False
					while_num = False
					break
			if indicate:
				print('\n Нет такого документа')
		else:
			print('\n Операция отменена')
			while_num = False
	# print_docs(my_docs)  # Для теста
	# print_dirs(my_dirs)  # Для теста
	return
	
# def change_dir(my_docs, my_dirs):
# 	print('\n Операция временно не доступна.')
# 	return
	
def change_dir(my_dirs):
	print('\n Перенос документа на другую полку (q - отмена).')
	ind_quite = True
	while_num = True
	while while_num:
		num_doc = input(' Введите номер документа: ')
		if num_doc.strip().lower() != 'q':
			old_shelf = None
			for key in my_dirs.keys():
				if num_doc in my_dirs[key]:
					old_shelf = key
			if old_shelf is not None:
				while_dir = True
				while while_dir:
					new_shelf = input(' Введите номер полки: ')
					if new_shelf.strip().lower() != 'q':
						if new_shelf != old_shelf:
							if new_shelf in my_dirs.keys():
								# Добавляем на новую полку
								my_dirs[new_shelf].append(num_doc)
								# Удаляем из старой полки
								my_dirs[old_shelf].remove(num_doc)
								print(f"\n Документ '{num_doc}' перенесён")
								while_dir = False
								while_num = False
								ind_quite = False
							else:
								print('\n Нет такой полки')
						else:
							print('\n Документ находится как раз на этой полке')
					else:
						# print('\n Операция отменена')
						while_num = False
						while_dir = False
			else:
				print('\n Нет такого документа')
		else:
			# print('\n Операция отменена')
			while_num = False
	if ind_quite:
		print('\n Операция отменена')
	# print_dirs(my_dirs)  # Для теста
	return

# def create_new_shelf(my_dirs):
# 	print('\n Операция временно не доступна.')
# 	return

def create_new_shelf(my_dirs):
	print('\n Создание новой полки (q - отмена).')
	ind_while = True
	while ind_while:
		new_shelf = input(' Введите номер для новой полки: ')
		if new_shelf.strip().lower() != 'q':
			if new_shelf not in my_dirs.keys():
				# Создаём новую полку
				my_dirs.update({new_shelf: []})
				print(f"\n Создана новая полка '{new_shelf}'")
				ind_while = False
			else:
				print('\n Такая полка уже существует')
		else:
			print('\n Операция отменена')
			ind_while = False
	# print_dirs(my_dirs)  # Для теста
	return


print('\n    Задача 1 и Задача 2. Раздел 1.5')
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

print('\n Исходные данные:')
print_docs(documents)
print_dirs(directories)

bool_repeat = True
while bool_repeat:
	print('\n Доступные команды:\n     p  - Чей документ\n     s  - Какая полка \
	\n     l  - Полный список документов\n     a  - Добавить новый документ \
	\n     d  - Удалить старый документ\n     m  - Переместить\
	документ на другую полку\n     as - Добавить новую полку\n     q  - Выход')
	assign = input('\n Ваш выбор: ')
	if assign == 'p':
		desiring_person(documents)
	elif assign == 's':
		desiring_shelf(directories)
	elif assign == 'l':
		listing_docs(documents)
	elif assign == 'a':
		create_new_doc(documents, directories)
	elif assign == 'd':
		delete_doc(documents, directories)
	elif assign == 'm':
		change_dir(directories)
	elif assign == 'as':
		create_new_shelf(directories)
	elif assign == 'q':  # quite_work 
		bool_repeat = False
	else:
		print(f" Неизвестная команда: '{assign}'")
	if bool_repeat:
		txt_inp = input('\n Хотите повторить? (y/n): ')
		if (str.upper(txt_inp) != 'Y') and (str.upper(txt_inp) != 'Д'):
			bool_repeat = False
# end while

print('\n -- Конец --')

# Для теста:
print('\n Окончательное состояние.')
print_docs(documents)
print_dirs(directories)

input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
