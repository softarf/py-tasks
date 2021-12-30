
# coding: utf-8        # -*- coding: utf-8 -*-

print('\n    Задача 3. Раздел 1.1\n')
salary = int(input(' Введите заработную плату в месяц: '))
mortgage = int(input(' Введите, какой процент(%) уходит на ипотеку: '))
living = int(input(' Введите, какой процент(%) уходит на жизнь: '))

year_salary = salary * 12
year_mortgage = int(year_salary * mortgage / 100)
accum = int(year_salary * (1 - living / 100) - year_mortgage)

print('\n Вывод:\n На ипотеку было потрачено:', year_mortgage, 'рублей')
print(' Было накоплено:', accum, 'рублей\n')

#print('\n  -- Конец --  ')  #                 - Для блокнота
input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
