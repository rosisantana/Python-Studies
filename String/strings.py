
name = 'ada lovelace'

#Utilizamos o método title(). Um método é uma ação que Python pode executar em um dado. O (.) após name em name.title() informa a Python que o método title() deve atuar na variável name. 

print(name.title())

#O método lower() é particularmente útil para armazenar dados. Muitas vezes, você fará a conversão das strings para letras minúsculas antes de armazená-las

print(name.upper())
print(name.lower())

#Podemos usar a concatenação para compor uma mensagem e então armazenar a mensagem completa em uma variável! Exemplo: 

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name

print('Primeiro nome:',first_name)
print('Sobrenome:', last_name)
print('Hello, ' + full_name.title() + '!')

message = 'Hello, ' +full_name.title() + '!'
print(message)

#Tabulações: \t 
print('Python')
print('\tTabulação Python')

#Quebra de linha: \n 
print('Languages:\nPython\nC\nJavascript')

#Quebra de linha + Tabulação: \n\t nova linha e a próxima com tabuação
print('Languages:\n\tPython\n\tC\n\tJavascript')

#No mundo real, essas funçõescde remoção são usadas com mais frequência para limpar entradas de usuário antes de armazená-las em um programa.

#Para garantir que não haja espaços em branco do lado direito de uma string, utilize o método rstrip(), lado esquerdo lstrip()

favorite_language = 'Python '

#Removendo o espaço de forma temporária:
favorite_language.rstrip()

#Removendo o espaço de forma permanente:
favorite_language = favorite_language.rstrip()





