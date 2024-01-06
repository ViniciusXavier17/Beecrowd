vetor = []
while len(vetor) < 10:
    n = int(input())
    if n <= 0:
        vetor.append(1)
    else:
        vetor.append(n)

for i, n in enumerate(vetor):
    print(f'X[{i}] = {n}')