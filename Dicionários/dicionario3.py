# Informações aninhadas. 
# Podemos aninhar um conjunto de dicionários em uma lista, uma lista de itens em um dicionário ou até mesmo um dicionário em um outro dicionário. 

#Uma lista de dicionários:

alien_0 = {'cor': 'verde', 'pontos': 5}
alien_1 = {'cor': 'amarelo', 'pontos': 10}
alien_2 = {'cor': 'vermelho', 'pontos': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print('\n\n')

# Gerando automaticamente cada alienigena usando range() para criar uma frota de 30 alienígenas: 

# Cria uma lista vazia para armazenar os alienígenas
aliens_frota = []

# Cria 30 alienígenas verdes
for alien_number in range(30):
    new_alien = {'cor': 'verde', 'pontos': 5, 'velocidade': 'devagar'}
    aliens_frota.append(new_alien)

# Mostra os 5 primeiros alienígenas:
for alien in aliens_frota[:5]:
    print(alien)
print('...')

# Mostra quantos aliens foram criados:
print('Número total de aliens na frota: ' + str(len(aliens_frota)))

# Todos esses alienígenas têm as mesmas características, mas Python considera cada um como um objeto diferente, o que nos permite modificar cada alienígena individualmente.

# Por exemplo, para mudar os três primeiros alienígenas para amarelo, com velocidade média, valendo dez pontos cada, podemos fazer o seguinte:

print('\n\n')

# Cria uma lista vazia para armazenar os alienígenas
aliens_frota = []

# Cria 30 alienígenas verdes
for alien_number in range(30):
    new_alien = {'cor': 'verde', 'pontos': 5, 'velocidade': 'devagar'}
    aliens_frota.append(new_alien)

for alien in aliens_frota[0:3]:
    if alien ['cor'] == 'verde':
        alien['cor'] = 'amarelo'
        alien['velocidade'] = 'media'
        alien['pontos'] = 10

# Mostra os 5 primeiros alienígenas:
for alien in aliens_frota[:5]:
    print(alien)
print('...')

print('\n\n')

# Poderíamos expandir esse laço acrescentando um bloco elif que transforme alienígenas amarelos em alienígenas vermelhos e rápidos, que valem 15 pontos cada.

for alien in aliens_frota[0:3]:
    if alien ['cor'] == 'verde':
        alien['cor'] = 'amarelo'
        alien['velocidade'] = 'media'
        alien['pontos'] = 10
    elif alien ['cor'] == 'amarelo':
        alien['cor'] = 'vermelho'
        alien['velocidade'] = 'rápido'
        alien['pontos'] = 15

# Mostra os 5 primeiros alienígenas:
for alien in aliens_frota[:5]:
    print(alien)
print('...')

print('\n\n\n----------------------------------------------------\n')


# Lista em um dicionário - Em vez de colocar um dicionário em uma lista, às vezes é conveniente colocar uma lista em um dicionário. 

# Armazena informações sobre uma pizza que está sendo pedida
pizza = {
    'massa': 'fina',
    'ingredientes': ['cheddar', 'cogumelos'],
}

# Resume o pedido: 
print('Você pediu uma pizza com massa ' + pizza['massa'] + ' e os ingredientes: ' )

for ingrediente in pizza['ingredientes']:
    print('\t' + ingrediente)


linguagens_favoritas = { 
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phill':['python', 'haskell'],
    'melisa':['javascript'],
    'jake': ['java', 'haskell', 'ruby']
}

for nome, linguagens in linguagens_favoritas.items():
    if len(linguagens) <= 1:
        print('\nA linguagem favorita da(o) ' + nome.title() + ' é:')
        for linguagem in linguagens:
            print('\t' + linguagem.title())
    else:
        print('\nAs linguagens preferidas do(a) ' + nome.title() + ' são: ')
        for linguagem in linguagens:
            print('\t' + linguagem.title())

# Um dicionário em um dicionário

users = { 
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())