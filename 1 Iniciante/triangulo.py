#include <stdio.h>
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
if a < (b + c) and b < (a + c) and c < (a + b):
    perimetro = a+b+c
    print(f'Perimetro = {perimetro:.1f}')
else:
    areaT = ((a+b) * c)/2
    print(f'Area = {areaT:.1f}')