def fibonacci(n):
    termo_anterior, termo_atual = 0, 1

    for i in range(n - 1):
        print(termo_anterior, end=" ")
        termo_anterior, termo_atual = termo_atual, termo_anterior + termo_atual
    print(termo_anterior)

n = int(input())

fibonacci(n)