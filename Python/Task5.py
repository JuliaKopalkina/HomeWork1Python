# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = []
Y = []
Z = []
LeftSide = not (X or Y or Z)
RightSide = not X and not Y and not Z 
if LeftSide == RightSide:
    print ('true')
else:
    print ('false')