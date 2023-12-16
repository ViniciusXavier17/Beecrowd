salario = input('')
salario = float(salario)
novo_salario = 0
percentual = 0
if salario <=400.00:
    novo_salario = (salario * 0.15) + salario
    percentual = 0.15

elif salario > 400.00 and salario <= 800.00:
    novo_salario = (salario * 0.12) + salario
    percentual = 0.12

elif salario > 800.00 and salario <=1200.00:
    novo_salario = (salario * 0.10) + salario
    percentual = 0.10

elif salario > 1200.00 and salario <=2000.00:
    novo_salario = (salario * 0.07) + salario
    percentual = 0.07

elif salario > 2000.00:
    novo_salario = (salario * 0.04) + salario
    percentual = 0.04


print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {salario * percentual:.2f}')
print(f'Em percentual: {percentual * 100:.0f} %')