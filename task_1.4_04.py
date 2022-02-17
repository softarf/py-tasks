
# coding: utf-8        # -*- coding: utf-8 -*-

print('\n    Задача 4. Раздел 1.4')
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

print('\n Исходные данные:\n stats = {', end='')
idx = 0
for channel, volume in stats.items():
   idx += 1
   if idx != 1:
       print(f",\n          '{channel}': {volume}", end='')
   else:
       print(f"'{channel}': {volume}", end='')
print('}')

print('\n Вывод:')
#stat_max = max(stats.items(), key=lambda x: x[1])           # Мой вариант
#print(f" Канал с максимальным объёмом: '{stat_max[0]}'")
stat_max = max(stats, key=stats.get)    # Вариант проверившего, Александр Бардин
print(f" Канал с максимальным объёмом: '{stat_max}'")

input('\n  -- Конец --  ')	#	Типа  "Пауза" - Для консоли
