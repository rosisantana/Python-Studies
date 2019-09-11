#Modificando elementos de uma lista

#Para alterar um elemento, use o nome da lista seguido do índice do elemento que você quer modificar e, então, forneça o novo valor que você quer que esse item tenha. Exemplo: 

motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

print('\nAlterando o índice [0] da lista:')
motocycles[0] = 'ducati'
print(motocycles)

#Quando concatenamos um item em uma lista, o novo elemento é inserido ao final. Exemplo: 

print('\nConcatenando elementos no final de uma lista:')
motocycles.append('honda')
print(motocycles)

print('\nIniciando uma lista vazia e acrescentando itens:')
cars = []
cars.append('ford')
cars.append('fiat')
cars.append('nissan')
print(cars)

#Inserindo elementos em uma lista

#Podemos adcionar um elemento novo em qualquer posição da lista usando o método insert().

#Essa operação desloca todos os demais valores da lista uma posição à direita Exemplo: 

print('\nAdicionando um elemento novo utilizando o método insert():')
cars.insert(0, 'volkswagen')
print(cars)

#Removendo elementos de uma lista

#Se a posição do item que você quer remover de uma lista for conhecida, a instrução del poderá ser usada. Exemplo:

print('\nRemovendo um elemento da lista utilizando del:')
del cars[3]
print(cars)

#Removendo com o método pop()

#O método pop() remove o último item de uma lista, mas permite que você trabalhe com esse item depois da remoção. O termo pop deriva de pensar em uma lista como se fosse uma pilha de itens e remover um item (fazer um pop) do topo da pilha. Nessa analogia, o topo da pilha corresponde ao final da lista.

print('\nNova lista:')
cars = ['fiat', 'ford', 'nissan']
print(cars)

print('\nRemovendo um elemento da lista utilizando o método pop()')
popped_cars = cars.pop()
print(cars)

print('\nUtilizando o item após a remoção. O item removido:')
print(popped_cars)












 