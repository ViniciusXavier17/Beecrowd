while True:
    quant = input()
    if quant == '0':
        break
    else:
        for i in range(int(quant)):
            lista_notas = input()
            lista_notas = lista_notas.split()
            lista_notas= list(map(int, lista_notas))
            resposta = []
            if lista_notas[0] <= 127:
                resposta.append('A')
            if lista_notas[1] <= 127:
                resposta.append('B')
            if lista_notas[2] <= 127:
                resposta.append('C')
            if lista_notas[3] <= 127:
                resposta.append('D')
            if lista_notas[4] <= 127:
                resposta.append('E')
            if len(resposta) > 1 or len(resposta) == 0:
                print('*')
            else:
                print(''.join(resposta))
