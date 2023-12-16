animais ={
    'aguia': ['vertebrado', 'ave', 'carnivoro'],
    'pomba': ['vertebrado', 'ave', 'onivoro'],
    'homem': ['vertebrado', 'mamifero', 'onivoro'],
    'vaca': ['vertebrado', 'mamifero', 'herbivoro'],
    'pulga': ['invertebrado', 'inseto', 'hematofago'],
    'lagarta': ['invertebrado', 'inseto', 'herbivoro'],
    'sanguessuga': ['invertebrado', 'anelideo', 'hematofago'],
    'minhoca': ['invertebrado', 'anelideo', 'onivoro']
}

c1 = input('')
c2 = input('')
c3 = input('')
lista_c = [c1, c2, c3]

for chaves, caracteristicas in animais.items():
    if caracteristicas == lista_c:
        print(chaves)
        break