
# coding: utf-8        # -*- coding: utf-8 -*-

print('\n    Задача 2. Раздел 1.1\n')
dim = input(' Введите длину стороны квадрата: ')

# Не знаю как реализовать анализ введённого значения на целое или вещественное не используя конструкцию if .

if dim.isdigit():
	side = int(dim)
else:
	side = float(dim)

perimeter = 4 * side
area = side ** 2
print('\n Вывод:\n Периметр:', perimeter, '\n Площадь:', area, '\n')

dim1 = input(' Введите длину прямоугольника: ')
if dim1.isdigit():
	length = int(dim1)
else:
	length = float(dim1)
dim2 = input(' Введите ширину прямоугольника: ')
if dim2.isdigit():
	width = int(dim2)
else:
	width = float(dim2)

perimeter = (length + width) * 2
area = length * width
print('\n Вывод:\n Периметр:', perimeter, '\n Площадь:', area, '\n')

#print('\n  -- Конец --  ')  #                 - Для блокнота
input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
