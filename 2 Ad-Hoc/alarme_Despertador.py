while True:
    H1, M1, H2, M2 = input('').split()
    H1 = int(H1)
    H2 = int(H2)
    M1 = int(M1)
    M2 = int(M2)
    if H1 == 0 and M1 == 0 and H2 == 0 and M2 == 0:
        break
    if H1 > H2 or H1 == H2 and M1 > M2:
        H2 += 24
    minutos = ((H2 * 60) + M2) - ((H1 * 60) + M1)
    print(minutos)