a, b = input('').split()
a, b = int(a), int(b)

print('Sao Multiplos') if b % a == 0 or a % b == 0 else print('Nao sao Multiplos')