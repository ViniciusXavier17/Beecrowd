vetor = []
n = int(input())
for i in range(10):
    vetor.append(n)
    n *= 2

for i, n in enumerate(vetor):
    print(f'N[{i}] = {n}')