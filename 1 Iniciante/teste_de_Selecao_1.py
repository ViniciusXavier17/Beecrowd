a, b,c, d = input('').split()
a, b, c, d = int(a), int(b), int(c), int(d)

c1 = b > c and d > a
c2 = c + d > a + b
c3 = c > 0 and d > 0
c4 = a % 2 == 0

if c1 and c2 and c3 and c4:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')