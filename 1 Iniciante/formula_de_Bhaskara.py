n1, n2, n3 =(input().split())
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)

delta = (n2**2 - 4 * n1 * n3)
if delta < 0:
    print('Impossivel calcular')
else:
    try:
        x1 = (-n2 + (delta**0.5)) / (2 * n1)
        x2 = (-n2 - (delta**0.5)) / (2 * n1)

        print(f'R1 = {x1:.5f}')
        print(f'R2 = {x2:.5f}')
    except ZeroDivisionError:
        print('Impossivel calcular')