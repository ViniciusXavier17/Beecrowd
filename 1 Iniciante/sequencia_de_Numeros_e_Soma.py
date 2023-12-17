while True:
    soma = 0
    n1, n2 = input().split()
    n1, n2 = int(n1), int(n2)

    if n1 <= 0 or n2 <= 0:
        break

    maior = max(n1, n2)
    menor = min(n1, n2)

    for i in range(menor, maior+1):
        soma = soma + i
        print(i , end=' ')

    print(f'Sum={soma}')