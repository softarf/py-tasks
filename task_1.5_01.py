
# coding: utf-8        # -*- coding: utf-8 -*-

def pr_queries(my_docs, my_dirs):
	print('\n Исходные данные:\n documents = [', end='')
	idx = 0
	for document in my_docs:
		idx += 1
		if idx != 1:
			print(f',\n     {document}', end='')
		else:
			print(f'\n     {document}', end='')
	print('\n    ]')
	print(' directories = {', end='')
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
	return
	
def desiring_shelf(my_dirs):
	indicate = True
	num_doc = input('\n Введите номер документа: ')
	for doc_key in my_dirs.keys():
		if num_doc in my_dirs[doc_key]:
			indicate = False
			print(f" Искомая полка: '{doc_key}'")
			break
	if indicate:
		print(f"\n Нет документа с номером '{num_doc}'")
	return
		
def listing_docs(my_docs):
	print('\n Имеются документы:\n')
	for document in my_docs:
		idx = 0
		for key in document.keys():
			idx += 1
			if idx != 1:
				print(f' "{document[key]}"', end=' ')
			else:
				print(f' {document[key]}', end=' ')
		print()
	return
		
def create_new_doc(my_docs, my_dirs):
	indicate = True
	print('\n Создание нового документа (q - отмена):')
	my_type = input(' Введите тип документа: ')
	if my_type.lower() != 'q' and indicate:
		pass
	else:
		indicate = False
	my_num = input(' Введите номер документа: ')
	if my_type.lower() != 'q' and indicate:
		pass
	else:
		indicate = False
	my_name = input(' Введите имя: ')
	if my_type.lower() != 'q' and indicate:
		pass
	else:
		indicate = False
	my_shelf = input(' Введите номер полки: ')
	if my_type.lower() != 'q' and indicate:
		pass
	else:
		indicate = False
	return


print('\n    Задача 1. Раздел 1.5')
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

pr_queries(documents, directories)

bool_repeat = True
while bool_repeat:
	print('\n Доступные команды:\n     p - Чей документ\n     s - Какая полка \
	\n     l - Полный список\n     a - Добавить новый документ\n     q - Выход')
	assign = input('\n Ваш выбор: ')
	if assign == 'p':
		desiring_person(documents)
	elif assign == 's':
		desiring_shelf(directories)
	elif assign == 'l':
		listing_docs(documents)
	elif assign == 'a':
		create_new_doc(documents, directories)
	elif assign == 'q':  # quite_work 
		bool_repeat = False
		print(' Вы ввели:', assign)
	else:
		print(f" Неизвестная команда: '{assign}'")
	if bool_repeat:
		txt_inp = input('\n Хотите повторить? (y/n): ')
		if (str.upper(txt_inp) != 'Y') and (str.upper(txt_inp) != 'Д'):
			bool_repeat = False
# end while

print('\n -- Конец --')

input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
