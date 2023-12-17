ii = 1
jj = 7
cont = 0
cont_g = 0
while True:

    print(f'I={ii} J={jj}')

    if cont == 2:
        cont_g += 1
        cont = 0
        ii += 2
        jj = ii + 6
    else:
        cont += 1
        jj -= 1
    
    if cont_g == 5:
        break