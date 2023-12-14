quant = input('')
quant = int(quant)
resultado = 0
for i in range(quant):
    equacao = input('')

    if equacao[0] == equacao[2]:
        resultado = int(equacao[0]) * int(equacao[2])
    elif equacao[1].isupper():
        resultado = int(equacao[2]) - int(equacao[0])
    elif equacao[1].islower():
        resultado = int(equacao[0]) + int(equacao[2])

    print(resultado)