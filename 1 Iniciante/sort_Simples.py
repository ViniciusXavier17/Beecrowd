n = input('')
lista = list(n.split())
lista_2 = list(map(int,lista.copy()))
lista_2.sort()
for n in lista_2:
    print(n)
print('')
for n in lista:
    print(n)