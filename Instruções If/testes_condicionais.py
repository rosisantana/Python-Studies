# O pequeno exemplo a seguir mostra como testes if
# permitem responder a situações especiais de forma correta.

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print('\n')

# No coração de cada instrução if está uma expressão que pode ser avaliada como True ou False ,chamada de teste condicional.

#Se um teste condicional for avaliado como True , Python executará o código após a instrução if . Se o teste for avaliado como False ,o interpretador ignorará o código depois da instrução if .

#Testes de Igualdade diferenciam letras maiúsculas de minúsculas.

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies!\n')

age = 18
print(age == 18)

answer = 17
if answer != 42:
    print('\nThat is not the correct answer. Please try again')

#Testando várias condições - As palavras reservadas and e or podem ajudar nessas situações.

age_0 = 22
age_1 = 18

print('\n')

if age_0 >= 21 and age_1 >= 21:
    print('Maiores que 21')
else:
    print('Menores que 21')

print('\n')

if age_0 >= 21 or age_1 >= 21:
    print('Maiores que 21')
else:
    print('Menores que 21')

#Verificando se um valor está em uma lista - Para descobrir se um valor em particular já está em uma lista, utilize a palavra reservada in:

print('\n')

requested_toppings = ['mushrooms', 'onions', 'pineapple']

if 'onions' in requested_toppings:
    print('Yes, Onions!')
else:
    print('No onions!')

if 'pepperoni' in requested_toppings:
    print('Yes, pepperoni!')
else:
    print('No pepperoni!')

#Verificando se um valor não está em uma lista - Podemos usar a palavra reservada not nesse caso.

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print('\n' + user.title() + ', you can post a response if you wish!')
