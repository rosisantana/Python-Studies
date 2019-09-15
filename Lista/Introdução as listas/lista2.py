#Modificando elementos de uma lista

#Para alterar um elemento, use o nome da lista seguido do índice do elemento que você quer modificar e, então, forneça o novo valor que você quer que esse item tenha. Exemplo: 

motorcycles= ['honda', 'yamaha', 'suzuki']
print(motorcycles)

print('\nAlterando o índice [0] da lista:')
motorcycles[0] = 'ducati'
print(motorcycles)

#Quando concatenamos um item em uma lista, o novo elemento é inserido ao final. Exemplo: 

print('\nConcatenando elementos no final de uma lista:')
motorcycles.append('honda')
print(motorcycles)

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
popped_cars = cars.pop() #Armazenando o elemento na variável
print(cars)

print('\nUtilizando o item após a remoção. O item removido:')
print(popped_cars) #Exibindo o elemento removido

#Você pode usar pop() para remover um item de qualquer posição em uma lista se incluir o índice do item que você deseja remover entre parênteses.

#Se você não tiver certeza se deve usar a instrução del ou o método pop(), eis um modo fácil de decidir: quando quiser apagar um item de uma lista e esse item não vai ser usado de modo algum, utilize a instrução del; se quiser usar um item à medida que removê-lo, utilize o método pop()

#Removendo um item de acordo com o valor

print('\nNova lista:')
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

print('\nRemovendo um item utilizando o método remove(), utilizado quando conhecemos o valor do item que desejamos remover.')
motorcycles.remove('ducati')
print(motorcycles)

#Também podemos utilizar o método remove() para trabalhar com um valor que está sendo removido da lista. 

print('\nNova lista:')
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles)

print('\nO valor "honda" foi armazenado em uma variável e utilizado na frase abaixo, além disso, foi retirado da lista:')
print('A moto ' + too_expensive.title() + ' é muito cara para mim!')
print(motorcycles)










 