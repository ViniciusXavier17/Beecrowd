PI = 3.14159
a, b, c = input('').split()
a, b, c = float(a), float(b), float(c)
a_triangulo_retangulo = (a * c) / 2
a_circulo = PI * c**2
a_trapezio = ((a + b) * c ) / 2
a_quadrado = b**2
a_retangulo = a * b

print(f'TRIANGULO: {a_triangulo_retangulo:.3f}')
print(f'CIRCULO: {a_circulo:.3f}')
print(f'TRAPEZIO: {a_trapezio:.3f}')
print(f'QUADRADO: {a_quadrado:.3f}')
print(f'RETANGULO: {a_retangulo:.3f}')