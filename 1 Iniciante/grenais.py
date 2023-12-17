total_inter = 0
total_grem = 0
total_jogos = 0
empates = 0
while True:
    inter, gremio = input().split()
    inter, gremio = int(inter), int(gremio)

    if inter > gremio:
        total_inter += 1
    elif gremio > inter:
        total_grem += 1
    else:
            empates += 1

    print('Novo grenal (1-sim 2-nao)')
    cont = input()

    if cont == '2':
        print(f'{total_jogos +1} grenais')
        print(f'Inter:{total_inter}')
        print(f'Gremio:{total_grem}')
        print(f'Empates:{empates}')
        if total_inter > total_grem:
            print('Inter venceu mais')
        elif total_grem > total_inter:
            print('Gremio venceu mais')
        else: 
            print('Nao houve vencedor')
        break
    elif cont == '1':
        total_jogos += 1