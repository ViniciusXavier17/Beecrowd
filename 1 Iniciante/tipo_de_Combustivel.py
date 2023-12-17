a, g, d= 0, 0,0
while True:
    valor = int(input())
    while valor < 1 or valor > 4:
        valor = int(input())
    if valor == 1:
        a += 1
    elif valor == 2:
        g += 1
    elif valor == 3:
        d += 1
    elif valor == 4: break

print('MUITO OBRIGADO')
print(f'Alcool: {a}')
print(f'Gasolina: {g}')
print(f'Diesel: {d}')