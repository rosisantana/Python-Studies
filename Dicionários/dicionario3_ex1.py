# Crie dois novos dicionários que representem pessoas diferentes e armazene os três dicionários em uma lista chamada people. Percorra sua lista de pessoas com um laço. À medida que percorrer a lista, apresente tudo que você sabe sobre cada pessoa.

usuario_0 = {
  'primeiro_nome': 'rosimeire',
  'sobrenome': 'santana',
  'idade': 24,
  'cidade': 'santo andré'
}

usuario_1 = {
    'primeiro_nome': 'danilo',
    'sobrenome': 'cutrim', 
    'idade': 24, 
    'cidade': 'são paulo'
}

usuario_2 = {
    'primeiro_nome': 'lupi',
    'sobrenome': 'lupinho',
    'idade': 3, 
    'cidade': 'sao bernardo'
}

usuarios = [usuario_0, usuario_1, usuario_2]

for usuario in usuarios:
    print(usuario)

print('\n')

