n = int(input())

for i in range(n):
    n1, n2, n3 = input().split()
    n1, n2, n3 = float(n1), float(n2), float(n3)
    media = (n1*2 + n2*3 + n3*5) / 10
    print(f'{media:.1f}')