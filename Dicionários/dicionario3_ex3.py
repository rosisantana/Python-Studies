# Lugares favoritos: Crie um dicionário chamado favorite_places. Pense em três nomes para usar como chaves do dicionário e armazene de um a três lugares favoritos para cada pessoa. Percorra o dicionário com um laço e apresente o nome de cada pessoa e seus lugares favoritos.

favorite_places = { 
    'amy': ['italia', 'espanha', 'marrocos'],
    'jake': ['chile'],
    'rosa': ['fortaleza', 'argentina'],
    'charles': ['nova iorque']
}

for name, places in favorite_places.items():
    if len(places) <= 1:
        print('\nO lugar favorito do(a) ' + name.title() + ' é:')
        for place in places: 
            print('\t' + place.title())
    else:
        print('\nOs lugares favoritos do(a) ' + name.title() + ' são:')
        for place in places: 
            print('\t' + place.title())