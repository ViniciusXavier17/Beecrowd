a, b, c = input().split()
a, b, c = float(a), float(b), float(c)
valores = [a, b, c]
valores.sort(reverse=True)
lista = []
for i in range(1):

    if valores[0] >= valores[1] + valores[2]:
        lista.append('NAO FORMA TRIANGULO')
        break
    
    if valores[0]**2 == valores[1]**2 + valores[2]**2:
        lista.append('TRIANGULO RETANGULO')

    if valores[0]**2 > valores[1]**2 + valores[2]**2:
        lista.append('TRIANGULO OBTUSANGULO')

    if valores[0]**2 < valores[1]**2 + valores[2]**2:
        lista.append('TRIANGULO ACUTANGULO')

    if valores[0] == valores[1] and valores[0] == valores[2] and valores[1] == valores[2]:
         lista.append('TRIANGULO EQUILATERO')
         break

    if valores[0] == valores[1] or valores[0] == valores[2] or valores[1] == valores[2]:
         lista.append('TRIANGULO ISOSCELES')

for i in lista:
    print(i)