n1 = int(input())
n2 = int(input())


if n1 < n2:
    for i in range(n1+1, n2):
        if i % 5 == 2 or i % 5 == 3:
            print(i)
else:
    for i in range(n2+1, n1):
        if i % 5 == 2 or i % 5 == 3:
            print(i)