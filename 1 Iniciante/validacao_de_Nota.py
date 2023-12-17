guarda_nota = []
while True:

    if len(guarda_nota) == 2:
        print(f'media = {sum(guarda_nota) / 2}')
        break

    nota = float(input())

    if nota < 0 or nota > 10:
        print('nota invalida')
        continue
    else:
        guarda_nota.append(nota)
        continue