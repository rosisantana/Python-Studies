#O tipo mais simples de instrução if tem um teste e uma ação

age = 19

if age >= 18:
  print('Para sua idade, o voto é obrigatório.')
  print('Você já fez o seu cadastro?')

#Um bloco if - else é semelhante a uma instrução if simples, porém a instrução else permite definir uma ação ou um conjunto de ações executado quando o teste condicional falhar.

print('\n')

age = 17

if age >= 18:
  print('Para sua idade, o voto é obrigatório.')
  print('Você já fez o seu cadastro?')
else:
  print('Você ainda é muito novo para votar.')
  print('Você pode se cadastrar assim que fizer 18 anos.')

#Muitas vezes, você precisará testar mais de duas situações possíveis; para avaliar isso, a sintaxe if - elif - else de Python poderá ser usada.

print('\n')

age = 67

if age < 4:
  print('Sua entrada no parque é gratuita.')
elif age < 18:
  print('Sua entrada no parque custa R$5,00')
else:
  print('Sua entrada no parque custa R$10,00')

#Outra forma de resolver:

if age < 4:
  price = 0
elif age < 18:
  price = 5
else:
  price = 10

print('\nSua entrada no parque custa R$' + str(price) + ',00')

#Usando vários blocos elif

if age < 4:
  price = 0
elif age < 18:
  price = 5
elif age < 65:
  price = 10
else:
  price = 5

print('\nSua entrada no parque custa R$' + str(price) + ',00')

#Python não exige um bloco else no final de uma cadeia if - elif . Às vezes, um bloco else é útil; outras vezes, é mais claro usar uma instrução elif adicional que capture a condição específica de interesse:

if age < 4:
  price = 0
elif age < 18:
  price = 5
elif age < 65:
  price = 10
elif age >= 65:
  price = 5

print('\nSua entrada no parque custa R$' + str(price) + ',00')

#Esse comportamento é vantajoso, pois é eficiente e permite testar uma condição específica. Às vezes, porém, é importante verificar todas as condições de interesse. Nesse caso, você deve usar uma série de instruções if simples, sem blocos elif ou else . Essa técnica faz sentido quando mais de uma condição pode ser True e você quer atuar em todas as condições que sejam verdadeiras.

print('\n----------------------------')
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
  print('Adicione mushrooms')
if 'pepperoni' in requested_toppings:
  print('Adicione pepperoni')
if 'extra cheese' in requested_toppings:
  print('Adicione extra cheese')

print('\nAcabamos de fazer a sua pizza!')

#Em suma, se quiser que apenas um bloco de código seja executado, utilize uma cadeia if - elif - else . Se mais de um bloco de código deveexecutar, utilize uma série de instruções if independentes.