#Trabalhando com parte de uma lista - um grupo específico de itens de uma lista, que Python chama de fatia.

#Fatiando uma lista - Para fatiar uma lista, especifique o índice do primeiro e do último elemento. Exemplo: os elementos 0, 1 e 2 serão devolvidos. 

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])

#Se o primeiro ou último índice de uma fatia for omitido, Python começará sua fatia automaticamente no início da lista

print(players[:2])
print(players[4:])

#se quisermos apresentar os três últimos jogadores da lista, podemos usar a fatia: 

print(players[-3:])
print('\n')

#Percorrendo uma fatia com um laço for - Você pode usar uma fatia em um laço for se quiser percorrer um subconjunto de elementos de uma lista.

print('Here are the first three players on my team:')
for player in players[:3]:
  print(player)

print('\n')

#Copiando uma lista

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

my_foods.append('cannoli')
friends_foods.append('ice cream')

print('\nMy favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)

#Isso não funciona: 
friends_foods = my_foods

#Agora, as duas variáveis apontam para a mesma lista:

print('\nMy favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_foods)


