vetor = []

n = float(input())
vetor.append(n)
for i in range(99):
    vetor.append(vetor[i] / 2)
    
j = 0
for i in vetor:
    
    print(f'N[{j}] = {i:.4f}')
    j += 1