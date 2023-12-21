quant = int(input(''))
quant_div = 0
for i in range(quant):
    numero = int(input(''))
    quant_div = 0
    for j in range(1, numero + 1):
        if numero % j == 0:
            quant_div += 1
    if quant_div == 2:
        print(f'{numero} eh primo')
    else:
        print(f'{numero} nao eh primo')