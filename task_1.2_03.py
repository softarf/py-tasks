'''
https://replit.com/@softar/HandyRelievedMigration#main.py
'''
# coding: utf-8        # -*- coding: utf-8 -*-

print('\n    Задача 3. Раздел 1.2\n')
input_month = input(' Введите месяц: ')
month = input_month.strip().lower()
day = int(input(' Введите число: '))
print('\n Вывод:')
if month == "март" and 21 <= day <= 31 or month == "апрель" and 1 <= day <= 20:
    print(' Овен')
elif month == "апрель" and 21 <= day <= 30 or month == "май" and 1 <= day <= 20:
    print(' Телец')
elif month == "май" and 21 <= day <= 31 or month == "июнь" and 1 <= day <= 21:
    print(' Близнецы')
elif month == "июнь" and 22 <= day <= 30 or month == "июль" and 1 <= day <= 22:
    print(' Рак')
elif month == "июль" and 23 <= day <= 31 or month == "август" and 1 <= day <= 23:
    print(' Лев')
elif month == "август" and 24 <= day <= 31 or month == "сентябрь" and 1 <= day <= 23:
    print(' Дева')
elif month == "сентябрь" and 24 <= day <= 30 or month == "октябрь" and 1 <= day <= 23:
    print(' Весы')
elif month == "октябрь" and 24 <= day <= 31 or month == "ноябрь" and 1 <= day <= 22:
    print(' Скорпион')
elif month == "ноябрь" and 23 <= day <= 30 or month == "декабрь" and 1 <= day <= 21:
    print(' Стрелец')
elif month == "декабрь" and 22 <= day <= 31 or month == "январь" and 1 <= day <= 20:
    print(' Козерог')
elif month == "январь" and 21 <= day <= 30 or month == "февраль" and 1 <= day <= 18:
    print(' Водолей')
elif month == "февраль" and 19 <= day <= 30 or month == "март" and 1 <= day <= 20:
    print(' Рыбы')
else:
    print(" Неправильня дата: '", input_month, "', ", day, sep='')

#print('\n  -- Конец --  ')  #                 - Для блокнота
input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
