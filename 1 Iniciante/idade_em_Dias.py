numero = int(input())
ano = numero // 365
mes = (numero % 365) // 30
dias = (numero % 365) % 30

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dias} dia(s)')