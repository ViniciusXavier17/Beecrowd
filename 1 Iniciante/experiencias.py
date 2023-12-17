quant = int(input())
total_cobaias= 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0

for i in range(quant):
    quant_c, raca = input().split()
    quant_c = int(quant_c)
    if raca == 'C':
        total_cobaias += quant_c
        total_coelhos += quant_c
    elif raca == 'S':
        total_cobaias += quant_c
        total_sapos += quant_c
    elif raca == 'R':
        total_cobaias += quant_c
        total_ratos += quant_c

print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {total_coelhos}')
print(f'Total de ratos: {total_ratos}')
print(f'Total de sapos: {total_sapos}')
print(f'Percentual de coelhos: {(total_coelhos / total_cobaias) * 100:.2f} %')
print(f'Percentual de ratos: {(total_ratos / total_cobaias) * 100:.2f} %')
print(f'Percentual de sapos: {(total_sapos / total_cobaias) * 100:.2f} %')