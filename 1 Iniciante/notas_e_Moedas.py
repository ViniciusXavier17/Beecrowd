cedulas, moedas = input().replace('.', ' ').split()
cedulas = int(cedulas)
moedas = int(moedas)
lista_cedulas = [100, 50, 20, 10, 5, 2, 1]
lista_moedas = [50, 25, 10, 5, 1]
print('NOTAS:')
for i in lista_cedulas:
    quant = cedulas // i
    cedulas = cedulas % i
    if i > 1:
        print(f'{quant} nota(s) de R$ {i}.00')
    if i == 1:
        print('MOEDAS:')
        print(f'{quant} moeda(s) de R$ {i}.00')
        for j in lista_moedas:
            quant = moedas // j
            moedas = moedas % j
            if j > 5:
                print(f'{quant} moeda(s) de R$ 0.{j}')
            if j <= 5:
                print(f'{quant} moeda(s) de R$ 0.0{j}')