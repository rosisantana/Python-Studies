#Olá admin: Crie uma lista com cinco ou mais nomes de usuários, incluindo o nome 'admin'. Suponha que você esteja escrevendo um código que exibirá uma saudação a cada usuário depois que eles fizerem login em um site. Percorra a lista com um laço e mostre uma saudação para cada usuário:

#Se o nome do usuário for 'admin', mostre uma saudação especial, por exemplo, Olá admin, gostaria de ver um relatório de status?

#Caso contrário, mostre uma saudação genérica, como Olá Eric, obrigado por fazer login novamente.

usuarios = ['rosa', 'jake', 'charles', 'amy', 'admin']

for usuario in usuarios:
  if usuario == 'admin':
    print('Olá '+ usuario +', gostaria de ver um relatório de status?')
  else:
    print('Olá ' + usuario.title() + ', obrigada por fazer login novamente.')

#Sem usuários: Acrescente um teste if para garantir que a lista de usuários não esteja vazia.

#Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns usuários!

#Remova todos os nomes de usuário de sua lista e certifique-se de que a mensagem correta seja exibida.

print('\n')

#usuarios = []

if usuarios:
  for usuario in usuarios:
    if usuario == 'admin':
      print('Olá '+ usuario +', gostaria de ver um relatório de status?')
    else:
      print('Olá ' + usuario.title() + ', obrigada por fazer login novamente.')
else:
  print('Precisamos encontrar alguns usuários!')

#Verificando nomes de usuários: Faça o seguinte para criar um programa que simule o modo como os sites garantem que todos tenham um nome de usuário único.

#Crie uma lista chamada current_users com cinco ou mais nomes de usuários.

#Crie outra lista chamada new_users com cinco nomes de usuários. Garanta que um ou dois dos novos usuários também estejam na lista current_users.

#Percorra a lista new_users com um laço para ver se cada novo nome de usuário já foi usado. Em caso afirmativo, mostre uma mensagem informando que a pessoa deverá fornecer um novo nome. Se um nome de usuário não foi usado, apresente uma mensagem dizendo que o nome do usuário está disponível.

#Certifique-se de que sua comparação não levará em conta as diferenças entre letras maiúsculas e minúsculas. Se 'John' foi usado, 'JOHN' não deverá ser aceito.

print('\n')

usuarios_atuais = ['jake', 'amy', 'rosa', 'charles', 'admin', 'terry']

novos_usuarios = ['gina', 'charles', 'scully', 'adrian', 'holt', 'Amy']

for usuario in novos_usuarios:
  if usuario.lower() in usuarios_atuais:
    print('Esse nome de usuário já existe! Informe um novo nome!')
  else:
    print('O nome ' + usuario + ' está disponível!')