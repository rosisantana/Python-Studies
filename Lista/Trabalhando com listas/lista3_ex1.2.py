#Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.

pizzas = ['marguerita', 'frango com catupiry', 'peperoni' ]

friend_pizzas = pizzas[:]

#Então, adicione uma nova pizza à lista original.

pizzas.append('napolitana')

#Adicione uma pizza diferente à lista friend_pizzas.

friend_pizzas.append('lombo')

#Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas favoritas são:; em seguida, utilize um laço for para exibir a primeira lista. Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize um laço for para exibir a segunda lista. Certifique-se de que cada pizza nova esteja armazenada na lista apropriada.

print('Minhas pizzas favoritas são: ')
print(pizzas)

print('\nAs pizzas favoritas do meu amigo são: ')
print(friend_pizzas)

#Escreva dois laços for para exibir cada lista de comidas.

print('\nMinhas pizzas favoritas são: ')
for pizza in pizzas:
  print(pizza.title())

print('\nAs pizzas favoritas do meu amigo são: ')
for friend in friend_pizzas:
  print(friend.title())

