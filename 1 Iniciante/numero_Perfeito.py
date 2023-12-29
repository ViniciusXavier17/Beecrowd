quant = int(input(''))
for i in range(quant):
    total = 0
    n = input('')
    for j in range(1, int(n)):
        if int(n) % j == 0:
            total = total + j
    if total == int(n):
        print(f'{n} eh perfeito')
    else:
        print(f'{n} nao eh perfeito')