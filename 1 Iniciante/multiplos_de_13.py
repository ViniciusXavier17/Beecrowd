soma = 0
n1= int(input(''))
n2 = int(input(''))

if n1 > n2:
    for i in range(n2, n1+1):
        if i % 13 != 0:
            soma += i
else:
    for i in range(n1, n2+1):
        if i % 13 != 0:
            soma += i

print(soma)