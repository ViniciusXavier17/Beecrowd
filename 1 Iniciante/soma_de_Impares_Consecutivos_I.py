def soma_impares_entre(x, y):
    soma = 0
    if x > y:
        x, y = y, x
    for i in range(x + 1, y):
        if i % 2 != 0:
            soma += i
    return soma

x = int(input())
y = int(input())

resultado = soma_impares_entre(x, y)
print(resultado)