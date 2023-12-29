def div():
    n = 0
    for i in range(2, 100+ 1):
        n += 1/i
    
    return n

n1 = 1 + div()
print(f'{n1:.2f}')
