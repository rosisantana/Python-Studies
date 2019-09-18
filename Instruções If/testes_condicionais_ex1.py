car = 'ford'
print('O carro é == ford? Eu acho que sim.')
print(car == 'ford')

print('O carro é == audi? Eu acho que não!')
print(car == 'audi')

pizza = 'marguerita'
print('A pizza é de Pepperoni? ')
print(pizza != 'marguerita')

cor = 'Amarelo'
print(cor.lower() == 'amarelo')

qtd = 6

if qtd < 5:
  print('Quantidade insuficiente!')
else:
  print('Quantidade ok!')

idade1 = 16
idade2 = 2

if idade1 >= 16 or idade2 >= 16:
  print('Um de vocês tem mais de 16 anos!')

if idade1 < 18 and idade2 < 18:
  print('Não podem dirigir!')
else:
  print('Apenas o mair de 18 anos pode dirigir')

cores = ['azul', 'amarelo', 'verde', 'vermelho']

if 'verde' in cores:
  print('Verde está na lista!')
else:
  print('Verde não está na lista')

if 'rosa' not in cores:
  print('Adicione a cor rosa a na sua lista!!!!')