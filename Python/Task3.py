# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

NumberOfQuarter = int(input( 'Введите номер четверти: '))

if NumberOfQuarter == 1:
    print ('В первой четверти Х > 0 и Y > 0')
elif NumberOfQuarter == 2:
    print ('Во второй четверти Х < 0 и Y > 0')
elif NumberOfQuarter == 3:
    print ('В третьей четверти Х < 0 и Y < 0')
elif NumberOfQuarter == 4:
    print ('В четвертой четверти Х > 0 и Y < 0')   
else:
    print ('Не является номером четверти')