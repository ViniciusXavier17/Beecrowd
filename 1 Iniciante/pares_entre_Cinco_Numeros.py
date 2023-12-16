quant_pares = 0
for i in range(5):
    n = input('')
    n = int(n)
    if n % 2 == 0:
        quant_pares += 1

print(f'{quant_pares} valores pares')