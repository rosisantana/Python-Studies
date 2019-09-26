# Percorrendo as chaves de um dicionário com um laço. 
# O método keys() é conveniente quando não precisamos trabalhar com todos os valores de um dicionário. 

favorite_language = {
    'jen': 'python', 
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_language.keys():
    print(name.title())

print('\n')

# O mesmo resultado é obtivo sem usar o keys()

for name in favorite_language:
    print(name.title())

print('\n')

for name in favorite_language.keys():
    print(name.title() + ', linguagem preferida: ' + favorite_language[name])

print('\n')

friends = ['phil', 'sarah']

for name in favorite_language.keys():
    print(name.title())

    if name in friends:
        print(' Olá ' + name.title() +
        ", aqui está marcado que sua linguagem favorita é " +
        favorite_language[name].title() + "!"
        )

print('\n')

# Podemos ver se um nome em especial não está na lista: 

if 'erin' not in favorite_language.keys():
    print('Erin, por favor responda a nossa enquete!')

# Percorrendo um dicionário em ordem usando laço
# Podemos usar a função sorted() para obter uma cópia ordenada das chaves

print('\n')

for name in sorted(favorite_language.keys()):
    print(name.title() + ', obrigada por responder a nossa enquete!')

# Percorrendo os valores de um dicionário com um laço
# O método values() pode ser usado para devolver uma lista de valores sem as chaves. 

print('\nAs linguagens mencionadas foram: ')

for language in favorite_language.values():
    print(language.title())

# Para ver cada linguagem escolhida sem repetições podemos utilizar um conjunto (set). Um conjunto é semelhante a uma lista, exceto que cada item de um conjunto deve ser único. 

print('\nAs linguagens mencionadas foram: ')

for language in set(favorite_language.values()):
    print(language.title())



