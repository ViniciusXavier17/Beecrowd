n1, n2, n3, n4 = input('').split()
n1, n2, n3, n4 = float(n1), float(n2), float(n3), float(n4)

media = (n1*2 + n2*3 + n3*4 + n4) / 10

if media >= 7.0:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
elif media < 5:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')
else:
    n_exame = float(input(''))
    media_final = (n_exame + media) / 2
    if media_final >= 5.0:
        print(f'Media: {media:.1f}')
        print(f'Aluno em exame.')
        print(f'Nota do exame: {n_exame:.1f}')
        print(f'Aluno aprovado.')
        print(f'Media final: {media_final:.1f}')
    else:
        print(f'Media: {media:.1f}')
        print(f'Aluno em exame.')
        print(f'Nota do exame: {n_exame:.1f}')
        print(f'Aluno reprovado.')
        print(f'Media final: {media_final:.1f}')