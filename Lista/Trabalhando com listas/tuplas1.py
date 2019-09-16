# As tuplas são listas imutáveis. 
# Para definí-las usamos parênteses ao invés de chaves e para acessar os índices usamos colchetes. 

#Se tivermos um retângulo que sempre deva ter determinado tamanho, podemos garantir que seu tamanho não mudará colocando as dimensões em uma tupla: 

dimensions = (200, 50)
print(dimensions)

#Percorrendo valores de uma tupla com um laço:

for dimension in dimensions:
  print(dimension)

#Sobrescrevendo uma tupla: Embora não seja possível modificar uma tupla, podemos atribuir um novo valor a uma variável que armazena uma tupla.

print('\n--Sobrescrevendo uma Tupla--')

print('Original dimensions:')
for dimension in dimensions:
  print(dimension)

dimensions = (400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
  print(dimension)

#Use-as quando quiser armazenar um conjunto de valores que não deva ser alterado durante a vida de um programa. 
