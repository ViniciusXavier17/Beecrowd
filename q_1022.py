from fractions import Fraction
quant = int(input(''))

for i in range(quant):
    e = input('').split(' ')
    if e[3] == '+':
        resultado1 = int(e[0]) * int(e[6]) + int(e[4]) * int(e[2])
        resultado2 = int(e[2]) * int(e[6])
        s = Fraction(resultado1, resultado2)
    elif e[3] == '-':
        resultado1 = int(e[0]) * int(e[6]) - int(e[4]) * int(e[2])
        resultado2 = int(e[2]) * int(e[6])
        s = Fraction(resultado1, resultado2)
    elif e[3] == '*':
        resultado1 = int(e[0]) * int(e[4])
        resultado2 = int(e[2]) * int(e[6])
        s = Fraction(resultado1, resultado2)
    else:
        resultado1 = int(e[0]) * int(e[6])
        resultado2 = int(e[4]) * int(e[2])
        s = Fraction(resultado1, resultado2)
    if '/' not in str(s):
        print(f'{resultado1}/{resultado2} = {s}/1')
    else:
        print(f'{resultado1}/{resultado2} = {s}')

