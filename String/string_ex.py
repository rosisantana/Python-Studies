nome = 'Rosi '
print('Alô ' + nome + ', você gostaria de aprender um pouco de Python hoje?\n')

primeiro_nome = 'rosimeire'
sobrenome = 'santana'
nome_completo = primeiro_nome + ' ' + sobrenome
print('Usando concatenação -> Nome: '+ nome_completo)
print('Usando o método upper() + concatenação -> ' + nome_completo.upper())
print('Usando o método lower() + concatenação -> ' + nome_completo.lower())
print('Usando o método title() + concatenação -> ' + nome_completo.title())

#Eis o modo de usar aspas simples e duplas corretamente:

print('\nO apóstrofo aparece entre um conjunto de aspas duplas, portanto o interpretador Python não terá nenhum problema para ler a string corretamente.')

citacao = '\nSteve Jobs: “Everybody in this country should learn to program a computer, because it teaches you how to think”'
print(citacao)

pessoa = 'Albert Einstein: '
message = '“Uma pessoa que nunca cometeu um erro jamais tentou nada novo.”'
print('\n' + pessoa + message)