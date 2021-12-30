
# coding: utf-8        # -*- coding: utf-8 -*-
'''
https://replit.com/@softar/PriceyGrayDatalogs#main.py

Не знал как правильно надо было организовать решение: Сначала вводятся все данные призывника,
а потом делается анализ на годен/не годен, и в какие войска. Или, по мере ввода,
сразу анализируется каждое введённое значени. Поэтому сделал оба варианта.
'''
#           Вариант 2

print('\n    Задача 2_v2. Раздел 1.2\n')
not_fit = True
height = int(input(' Введите рост призывника: '))
if height >= 160:
  old = int(input(' Введите возраст призывника: '))
  if 18 <= old <= 27:
    children = int(input(' Укажите количество детей: '))
    if children < 2:
      isstudent = input(' Учится ли он сейчас (y/n): ').lower()
      if isstudent == 'n':
        not_fit = False
        if 160 <= height <= 169:
          print('\n Годен. Танковые войска.\n')
        elif 170 <= height <= 179:
          print('\n Годен. Морской флот.\n')
        elif 180 <= height <= 200:
          print('\n Годен. Десантные войска.\n')
        elif height > 200:
          print('\n Годен. Другие войска.\n')
if not_fit:
  print('\n К службе не годен.')

#print('\n  -- Конец --  ')  #                 - Для блокнота
input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для среды
