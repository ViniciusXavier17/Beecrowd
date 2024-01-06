vetor = []
for i in range(100):
    n = float(input())
    vetor.append(n)

for i, n in enumerate(vetor):
    if n <= 10:
        print(f'A[{i}] = {n:.1f}')