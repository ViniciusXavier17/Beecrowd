quant_pares = 0
quant_impares = 0
quant_positivos = 0
quant_negativos = 0
for i in range(5):
    n = input('')
    n = int(n)
    if n % 2 == 0:
        quant_pares += 1
    elif n % 2 !=0:
        quant_impares += 1

    if n > 0:
        quant_positivos += 1
    elif n < 0:
        quant_negativos += 1


print(f'{quant_pares} valor(es) par(es)')
print(f'{quant_impares} valor(es) impar(es)')
print(f'{quant_positivos} valor(es) positivo(s)')
print(f'{quant_negativos} valor(es) negativo(s)')