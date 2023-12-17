def calcula_media():
    guarda_nota = []
    while True:

        if len(guarda_nota) == 2:
            print(f'media = {sum(guarda_nota) / 2:.2f}')
            break
                
        nota = float(input())

        if nota < 0 or nota > 10:
            print('nota invalida')
            continue
        else:
            guarda_nota.append(nota)
            continue
        

calcula_media()

while True:
    print('novo calculo (1-sim 2-nao)')
    cont = input('')
    if cont == '1':
        calcula_media()
    elif cont == '2':
        break
    else:
        continue