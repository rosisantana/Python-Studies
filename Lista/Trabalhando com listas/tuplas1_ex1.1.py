#Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos básicos de comida. Pense em cinco pratos  e armazene-os em uma tupla.

print('Cardápio:')
comidas = ('macarronada', 'parmegiana', 'estrogonofe', 'arroz de forno', 'legumes sauté')

#Use um laço for para exibir cada prato oferecido pelo restaurante.

for comida in comidas:
  print(comida.title())

#Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.

#comidas[3] = 'lasanha'

#O restaurante muda seu cardápio, substituindo dois dos itens com pratos diferentes. Acrescente um bloco de código que reescreva a tupla e, em seguida, use um laço for para exibir cada um dos itens do cardápio revisado.

print('\nNovo cardápio:')
comidas = ('macarronada', 'milanesa', 'estrogonofe', 'lasanha', 'legumes sauté')
for comida in comidas:
  print(comida.title())
