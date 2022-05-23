# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

print('Координаты точки А:')
CoordinateX1 = int(input( 'Введите координату Х1: '))
CoordinateY1 = int(input( 'Введите координату Y1: '))
print('Координаты точки В:')
CoordinateX2 = int(input( 'Введите координату Х2: '))
CoordinateY2 = int(input( 'Введите координату Y2: '))

import math
Distance = math.sqrt((CoordinateX1-CoordinateX2)**2 + (CoordinateY1-CoordinateY2)**2)

print ('Расстояние между точками А и В:')
print ('%.2f'% Distance)