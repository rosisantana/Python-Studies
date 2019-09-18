#Cores de alienígenas #1: Suponha que um alienígena acabou de ser atingido em um jogo. Crie uma variável chamada alien_color e  atribua-lhe um valor igual a 'green', 'yellow' ou 'red'.

#Escreva uma instrução if para testar se a cor do alienígena é verde. Se for, mostre uma mensagem informando que o jogador acabou de ganhar cinco pontos.

alien_color = 'grey'

if alien_color == 'green':
  print('Você ganhou 5 pontos!')

#Escreva uma versão desse programa que execute o bloco if e outro que execute o bloco else. Se a cor não for verde, informe que o jogador ganhou 10 pontos.

if alien_color == 'green':
  print('Você ganhou 5 pontos')
else: 
  print('Você ganhou 10 pontos!')

#Se o alienígena for verde, mostre uma mensagem informando que o jogador ganhou cinco pontos.

#Se o alienígena for amarelo, mostre uma mensagem informando que o jogador ganhou dez pontos.

#Se o alienígena for vermelho, mostre uma mensagem informando que o jogador ganhou quinze pontos.

#Escreva três versões desse programa, garantindo que cada mensagem seja exibida para a cor apropriada do alienígena.


#Versão 1:

if alien_color == 'green':
  print('Você ganhou 5 pontos')
elif alien_color == 'yellow':
  print('Você ganhou 10 pontos')
else:
  print('Você ganhou 15 pontos')

#Versão 2:

if alien_color == 'green':
  pontos = 5
elif alien_color == 'yellow':
  pontos = 10
else:
  pontos = 15

print('\nVocê ganhou ' + str(pontos) + ' pontos')

#Versão 3:

if alien_color == 'green':
  pontos = 5
elif alien_color == 'yellow':
  pontos = 10
elif alien_color == 'red':
  pontos = 15

print('\nVocê ganhou ' + str(pontos) + ' pontos!')

