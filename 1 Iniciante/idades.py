n = 0
soma = 0
quant = 0
while n >= 0:
    n = int(input())
    if n >= 0:
        soma += n
        quant += 1

media = soma/quant
print(f'{media:.2f}')