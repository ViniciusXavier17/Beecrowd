n = input()

for i in range(int(n)+1):
    if i > 0 and i % 2 == 0:
        print(f'{i}^2 = {i**2}')