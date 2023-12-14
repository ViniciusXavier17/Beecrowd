while True:
    quant = input()
    if int(quant) == 0:
        break
    resultados = input().split()
    resultados = list(map(int, resultados))
    m = 0
    j = 0
    for i in range(int(quant)):
        if resultados[i] == 0:
            m += 1
        elif resultados[i] == 1:
            j += 1
    print(f'Mary won {m} times and John won {j} times')