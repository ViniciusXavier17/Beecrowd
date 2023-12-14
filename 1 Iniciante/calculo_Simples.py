cod_1, quant_1, valor_1 = input('').split()
cod_2, quant_2, valor_2 = input('').split()

valor_total = (float(valor_1) * int(quant_1)) + (float(valor_2) * int(quant_2)) 

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')