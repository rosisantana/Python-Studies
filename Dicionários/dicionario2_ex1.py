# Rios: Crie um dicionário que contenha três rios importantes e o país que cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'. 
#  Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre pelo Egito.

rios = {
    'amazonas': 'brasil',
    'nilo': 'egito',
    'yangtzé': 'china',
}

for rio in rios:
    print('O Rio ' + rio + ' corre pelo ' + rios[rio].title())


# Use um laço para exibir o nome de cada rio incluído no dicionário.

print('\nOs rios mencionados:')

for rio in rios.keys():
    print('Rio ' + rio.title())

# Use um laço para exibir o nome de cada país incluído no dicionário.

print('\nOs países mencionados:')

for pais in rios.values():
    print(pais.title())