favorite_language = {
    'jen': 'python', 
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Crie uma lista de pessoas que devam participar da enquete sobre linguagem favorita. Inclua alguns nomes que já estejam no dicionário e outros que não estão.

names = ['may', 'phil', 'veronica', 'jen']

# Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem respondido à enquete, mostre uma mensagem agradecendo-lhes por responder.

# Se ainda não participaram da enquete, apresente uma mensagem convidando-as a responder.

for name in names:
    if name in favorite_language:
        print('Obrigada por responder a enquete, ' + name.title() + '.')
    else:
        print(name.title() + ', você poderia responder a nossa enquete por favor ?')

