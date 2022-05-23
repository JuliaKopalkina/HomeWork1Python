# Напишите программу, которая принимает на вход координаты 
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти 
# плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

CoordinateX = int(input( 'Введите координату Х: '))
CoordinateY = int(input( 'Введите координату Y: '))

if CoordinateX > 0 and CoordinateY > 0:
    print ('1 четверть')
elif CoordinateX > 0 and CoordinateY < 0:
    print ('4 четверть')
elif CoordinateX < 0 and CoordinateY > 0:
    print ('2 четверть')
elif CoordinateX < 0 and CoordinateY < 0:
    print ('3 четверть')
elif CoordinateX == 0 and CoordinateY == 0:
    print ('Начало координат')
elif CoordinateX != 0 and CoordinateY == 0:
    print ('Ось абсцисс')
elif CoordinateX == 0 and CoordinateY != 0:
    print ('Ось ординат')