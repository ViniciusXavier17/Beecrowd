quant = int(input())

for i in range(quant):
    x , y = input().split()
    x, y = int(x), int(y)
    try:
        print(x/y)
    except ZeroDivisionError:
        print('divisao impossivel')