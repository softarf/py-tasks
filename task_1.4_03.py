
# coding: utf-8        # -*- coding: utf-8 -*-

print('\n    Задача 3. Раздел 1.4')
queries = [
           'смотреть сериалы онлайн',
           'новости спорта',
           'афиша кино',
           'курс доллара',
           'сериалы этим летом',
           'курс по питону',
           'сериалы про спорт сериалы про спорт сериалы про спорт сериалы про спорт',  # Для теста
           'сериалы про спорт сериалы про спорт сериалы про спорт сериалы',  # Для теста
           'сериалы про спорт'
           ]
print('\n Исходные данные:\n queries = {', end='')
total = 0
for item in queries:
   total += 1
   if total != 1:
       print(f",\n            '{item}'", end='')
   else:
       print(f"'{item}'", end='')
print('}')
len_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for item in queries:
	len_queries = len(item.split())
	if len_queries <= 10:
		len_list[len_queries-1] += 1
	else:
		len_list[10] += 1
#	
print(f'\n total = {total}\n len_list = {len_list}')  # Для теста
#
print('\n Вывод:')
for index in range(10):
	if len_list[index] > 0:
		percen = len_list[index] / total
		print(f' Запросов из {index+1} слов', '\t-', f' {percen: .0%}')
if len_list[10] > 0:
	percen = len_list[10] / total
	print(f' Запросов длиною свыше 10-ти слов - {percen: .0%}')

input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
