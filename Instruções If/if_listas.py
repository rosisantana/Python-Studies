ingredientes = ['queijo', 'calabreza', 'cebola']

for ingrediente in ingredientes:
  print('Adicionando ' + ingrediente + '.')

print('Pizza pronta!\n')

#E se a pizzaria ficasse sem tomates ? 

for ingrediente in ingredientes:
  if ingrediente == 'cebola':
    print('Desculpe, estamos sem '+ ingrediente + ' no momento!')
  else:
    print('Adicionando ' + ingrediente + '.')

print('Pizza pronta!\n')

#Verificando se uma lista não está vazia - Quando o nome de uma lista é usado em uma instrução if ,Python devolve True se a lista contiver pelo menos um item; uma lista vazia é avaliada como False.

ingredientes = []

if ingredientes:
  for ingrediente in ingredientes:
    print('Adicionando ' + ingrediente + '.')
  print('Pizza pronta!\n')
else:
  print('Tem certeza que você quer uma pizza simples?\n')

ingredientes_disponiveis = ['queijo', 'calabresa', 'cebola','pepperoni', 'catupiry', 'lombo']

ingredientes_solicitados = ['lombo', 'catupiry', 'berinjela']

for ingrediente in ingredientes_solicitados:
  if ingrediente in ingredientes_disponiveis:
    print('Adicionando ' + ingrediente + '.')
  else:
    print('Desculpe, nós não temos ' + ingrediente + '.')

print('Pizza pronta!\n')