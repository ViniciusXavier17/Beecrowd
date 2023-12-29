from functools import reduce

n = int(input())

lista = [j for j in range(1, n + 1)]

n1 = reduce(lambda x,y: x * y, lista)
print(n1)