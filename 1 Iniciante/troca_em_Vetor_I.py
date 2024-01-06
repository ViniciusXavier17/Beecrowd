vetor = []
for i in range(20):
    n = int(input())
    vetor.append(n)

vetor = reversed(vetor)
for i, n in enumerate(vetor):
    print(f'N[{i}] = {n}')