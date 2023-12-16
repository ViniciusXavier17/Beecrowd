quant = int(input(''))
in_n = 0
out_n = 0
for i in range(quant):
    n = int(input(''))
    if n >=10 and n <=20:
        in_n += 1
    else: 
        out_n += 1

print(f'{in_n} in')
print(f'{out_n} out')