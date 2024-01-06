vetor = []

n = int(input())
n2 = 0
for i in range(1000):
    print(f'N[{i}] = {n2}')
    n2 += 1
    if n2 == n:
        n2 = 0