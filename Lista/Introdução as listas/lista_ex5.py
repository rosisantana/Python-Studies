#Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que você gostaria de visitar. Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em ordem alfabética.
print('Cinco lugares do mundo: ')
world = ['italia', 'bali', 'peru', 'japao', 'hawai']
print(world)

#Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a lista propriamente dita.
print('\nLista em ordem alfabética: ')
print(sorted(world))

print('\nLista em ordem original:')
print(world)

#Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar a ordem da lista original.
print('\nLista em ordem alfabética inversa: ')
print(sorted(world, reverse=True))

print('\nLista em ordem original:')
print(world)

#Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar que sua ordem mudou.
print('\nLista em ordem inversa (não alfabética!)')
world.reverse()
print(world)

#Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para mostrar que ela voltou à sua ordem original.
print('\nAplicando a ordem inversa novamente voltamos a lista original:')
world.reverse()
print(world)

#Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.
world.sort()
print('\nLista em ordem alfabética de forma permanente: ')
print(world)

#Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou 
world.sort(reverse=True)
print(world)

#Convidados para o jantar: Trabalhando com um dos programas dos Exercícios 4, use len() para exibir uma mensagem informando o número de pessoas que você está convidando para o jantar.
dinner = ['gina', 'charles', 'amy']
qtd = len(dinner)
print('\n' + str(qtd) + ' pessoas foram convidadas para o jantar!')
