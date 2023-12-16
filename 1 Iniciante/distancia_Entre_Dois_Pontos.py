x1, y1 = input('').split()
x2, y2 = input('').split()
x1, x2 = float(x1), float(x2)
y1, y2 = float(y1), float(y2)

distancia_x = (x2 - x1)**2
distancia_y = (y2 - y1)**2
soma = (distancia_x + distancia_y)**0.5

print(f'{soma:.4f}')