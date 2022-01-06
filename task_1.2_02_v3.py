
# coding: utf-8        # -*- coding: utf-8 -*-
'''
https://replit.com/@softar/PriceyGrayDatalogs#main.py

Каждое введённое значени анализируется по мере ввода.
'''
#           Вариант 3  Постепенный ввод данных призывника, анализ if-elif (не полный)

print('\n    Задача 2_v3. Раздел 1.2\n')
not_fit = True
height = int(input(' Введите рост призывника: '))
if height < 160:
    pass
elif not (18 <= int(input(' Введите возраст призывника: ')) <= 27):
    # В Python работает только конструкция "Вхождение в интервал", потому что:  18 < old < 27  ==>  (old > 18) and (old < 27)
    # Конструкция "НЕвхождение в интервал" не работает!, потому что:            18 > old > 27  ==>  (old < 18) and (old > 27)
    pass
elif int(input(' Укажите количество детей: ')) >= 2:
    pass
elif input(' Учится ли он сейчас (y/n): ').lower() == 'n':
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
