# Animais de estimação: Crie vários dicionários, em que o nome de cada dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua o tipo do animal e o nome do dono. Armazene esses dicionários em uma lista chamada pets. Em seguida, percorra sua lista com um laço e, à medida que fizerisso, apresente tudo que você sabe sobre cada animal de estimação.

lupi = {'tipo': 'cachorro', 'dono': 'rosi'}
frederico = {'tipo': 'gato', 'dono': 'kézia'}
maggie = {'tipo': 'cachorro', 'dono': 'danilo'}

pets = [lupi, maggie, frederico]

for pet in pets: 
    print(pet)