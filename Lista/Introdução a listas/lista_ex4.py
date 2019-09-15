#Crie uma lista que inclua pelo menos três pessoas para jantar. Em seguida, utilize sua lista para exibir uma mensagem para cada pessoa, convidando-a para jantar.
dinner = ['gina', 'charles', 'amy']

print('\nHey, ' + dinner[0].title() + '! que tal jantar com os amigo quinta à noite ?')
print('Hey, ' + dinner[1].title() + '! que tal jantar com os amigo quinta à noite ?')
print('Hey, ' + dinner[2].title() + '! que tal jantar com os amigo quinta à noite ?')

#Alterando a lista de convidados: Você acabou de saber que um de seus convidados não poderá comparecer ao jantar, portanto será necessário enviar um novo conjunto de convites. Você deverá pensar em outra pessoa para convidar.

#Acrescente uma instrução print no final de seu programa, especificando o nome do convidado que não poderá comparecer.
print('\nInfelizmente ' + dinner[2].title() + ' não poderá vir! :(')

#Modifique sua lista, substituindo o nome do convidado que não poderá comparecer pelo nome da nova pessoa que você está convidando.
dinner[2] = 'terry'

#Exiba um segundo conjunto de mensagens com o convite, uma para cada pessoa que continua presente em sua lista.
print('\nHey, ' + dinner[0].title() + '! que tal jantar com os amigo quinta à noite ?')
print('Hey, ' + dinner[1].title() + '! que tal jantar com os amigo quinta à noite ?')
print('Hey, ' + dinner[2].title() + '! que tal jantar com os amigo quinta à noite ?')

#Mais convidados: Você acabou de encontrar uma mesa de jantar maior,portanto agora tem mais espaço disponível. Pense em mais três convidados para o jantar.

#Acrescente uma instrução print no final de seu programa informando às pessoas que você encontrou uma mesa de jantar maior.
print('\nBoas notícias! Conseguimos uma mesa maior! (Uhul)')

#Utilize insert() para adicionar um novo convidado no início de sua lista. Utilize insert() para adicionar um novo convidado no meio de sua lista. Utilize append() para adicionar um novo convidado no final de sua lista.
dinner.insert(0, 'jake')
dinner.insert(1, 'ray holt')
dinner.append('rosa')

#Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que está em sua lista.
print('\nHey, ' + dinner[0].title() + '! que tal jantar com os amigo quinta à noite ?')
print('Hey, ' + dinner[1].title() + '! que tal jantar com os amigo quinta à noite ?')
print('Hey, ' + dinner[2].title() + '! que tal jantar com os amigo quinta à noite ?')
print('Hey, ' + dinner[3].title() + '! que tal jantar com os amigo quinta à noite ?')
print('Hey, ' + dinner[4].title() + '! que tal jantar com os amigo quinta à noite ?')
print('Hey, ' + dinner[5].title() + '! que tal jantar com os amigo quinta à noite ?')

#Reduzindo a lista de convidados: Você acabou de descobrir que sua nova mesa de jantar não chegará a tempo para o jantar e tem espaço para somente dois convidados.

#Acrescente uma nova linha que mostre uma mensagem informando que você pode convidar apenas duas pessoas para o jantar.
print('\nBad news! Apenas duas pessoas poderão ir ao jantar! :(')

#Utilize pop() para remover os convidados de sua lista, um de cada vez, até que apenas dois nomes permaneçam em sua lista. Sempre que remover um nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela saiba que você sente muito por não poder convidá-la para o jantar.
out = dinner.pop()
print('\nSinto muito por não poder te convidar para o jantar, ' + out.title() + '!')

out = dinner.pop()
print('Sinto muito por não poder te convidar para o jantar, ' + out.title() + '!')

out = dinner.pop()
print('Sinto muito por não poder te convidar para o jantar, ' + out.title() + '!')

out = dinner.pop()
print('Sinto muito por não poder te convidar para o jantar, ' + out.title() + '!')

#Apresente uma mensagem para cada uma das duas pessoas que continuam na lista, permitindo que elas saibam que ainda estão convidadas.
print('\nHey, ' + dinner[0].title() + '! que tal jantar com os amigo quinta à noite ?')
print('Hey, ' + dinner[1].title() + '! que tal jantar com os amigo quinta à noite ?')

#Utilize del para remover os dois últimos nomes de sua lista, de modo que você tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem uma lista vazia no final de seu programa.
del dinner[0]
del dinner[0]
print(dinner)