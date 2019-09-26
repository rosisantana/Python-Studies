# Um dicionário em Python é uma coleção de pares chave-valor. Cada chave é conectada a um valor, e você pode usar uma chave para acessar o valor associado a ela.

# O valor de uma chave pode ser um número, uma string, uma lista ou até mesmo outro dicionário.

# Em Python, um dicionário é representado entre chaves, {} , com uma série de pares chave-valor entre elas.

# O dicionário alien_0 armazena a cor do alienígena e o valor da pontuação:

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print('Você ganhou ' + str(new_points) + ' pontos!')

# Adicionando novos pares chave-valor - para acrescentar um novo par chave-valor, especifique o nome do dicionário, seguido da nova chave entre colchetes, juntamente com o novo valor.

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Começando com um dicionário vazio - Para começar a preencher um dicionário vazio, defina-o com um conjunto de chaves vazio e depois acrescente cada par chave-valor em sua própria linha.

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modificando valores em um dicionário - especifique o nome do dicionário com a chave entre colchetes e o novo valor que você quer associar a essa chave.

alien_0 = {'color': 'verde'}
print('O alien é ' + alien_0['color'] + '.')

alien_0['color'] = 'amarelo'
print('O alien agora é ' + alien_0['color'] + '.\n')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('Posição x original = ' + str(alien_0['x_position']))

# Move o alienígena para a direita
# Determina a distância que o alienígena deve se deslocar de acordo com sua velocidade atual.

if alien_0['speed'] == 'slow':
  x_increment = 1
elif alien_0['speed'] == 'medium':
  x_increment = 2
else:
  x_increment = 3

# A nova posição é a posição antiga somada ao incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("Posição x atual = " + str(alien_0['x_position']))

# Podemos utilizar a instrução del para remover totalmente um par chave-valor. Para isso precisamos do nome do dicionário e da chave que queremos remover.

alien = {'cor': 'verde', 'pontos': 10}
print(alien)

del alien['pontos']
print(alien , '\n')

# Um dicionário de objetos semelhantes

#Também podemos utilizar o dicionério para guardar informações sobre diversos objetos: 

favorite_languages = { 
  'jen': 'python', 
  'sarah': 'c',
  'edward': 'ruby', 
  'phil': 'python',
}

print('A linguagem preferida de Sarah é ' +
  favorite_languages['sarah'].title() +
  '.')

