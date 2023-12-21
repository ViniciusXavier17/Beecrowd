def div():
    n1, n2 = 3, 2
    divisao = 0
    while n1 != 39:
        divisao += n1/n2
        n1 += 2
        n2 *= 2
        
    
    return divisao

n1 = 1 + div()
print(f'{n1:.2f}')