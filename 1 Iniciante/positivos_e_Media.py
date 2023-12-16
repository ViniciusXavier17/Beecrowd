quant_p = 0
soma = 0
for i in range(6):
    n = input('')
    m = float(n)
    if m > 0:
        quant_p += 1
        soma += float(n)

print(f'{quant_p} valores positivos')
print(f'{soma / quant_p:.1f}')