#Organizando uma lista: Com frequência, suas listas serão criadas em uma ordem imprevisível, pois nem sempre você poderá controlar a ordem em que seus usuários fornecem seus dados. 

#Método sort() 
print('Itens em ordem alfabética de forma permanente com sort():')
print('Nova lista:')
cars = ['bmw', 'audi', 'toyota', 'sabaru']
print(cars)
print('\nAplicando sort():')
cars.sort()
print(cars)

print('\nOrdem alfabética inversa com o argumento reverse=True:')
cars = ['bmw', 'audi', 'toyota', 'sabaru']
print('Aplicando o argumento reverse=True ao método sort():')
cars.sort(reverse=True)
print(cars)

#Ordenando uma lista temporariamente com a função sorted()
#Para preservar a ordem original de uma lista, mas apresentá-la de forma ordenada, podemos usar a função sorted() 

print('\nOrdenando a lista temporariamente com a função sorted:')
print('Lista original: ')
cars = ['bmw', 'audi', 'toyota', 'sabaru']
print(cars)

print('\nUtilizando a função sorted(): ')
print(sorted(cars))

print('\nLista original novamente: ')
cars = ['bmw', 'audi', 'toyota', 'sabaru']
print(cars)

#Essa função também pode aceitar um argumento reverse=True se você quiser exibir uma lista em ordem alfabética inversa.

print('Exibindo uma lista em ordem inversa com reverse():')
print('\nLista original: ')
cars = ['bmw', 'audi', 'toyota', 'sabaru']
print(cars)
cars.reverse()
print('\nLista em ordem inversa: ')
print(cars)

#Observe que reverse() não reorganiza em ordem alfabética inversa; ele simplesmente inverte a ordem da lista. De forma permanente, mas para restaurar, basta aplicar o reverse novamente. 

print('\nDescobrindo o tamanho de uma lista com a função len():')
print('\nLista original: ')
cars = ['bmw', 'audi', 'toyota', 'sabaru']
print(cars)
tamanho = len(cars)
print('Tamanho da lista = ' + str(tamanho))

#Python conta os itens de uma lista começando em um, portanto você não deverá se deparar com nenhum erro de deslocamento de um ao determinar o tamanho de uma lista.


