while True:
    try:
        ang = int(input(""))

        print('Y') if ang % 6 == 0 else print('N')
    except EOFError:
        break