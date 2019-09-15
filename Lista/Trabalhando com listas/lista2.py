#Criando listas numéricas

#A função range() de Python facilita gerar uma série de números.

for value in range(1,6):
  print(value)

#A função range() faz Python começar a contar no primeiro valor que você lhe fornecer e parar quando atingir o segundo valor especificado. Como ele para nesse segundo valor, a saída não conterá o valor final.

#Se quiser criar uma lista de números, você pode converter os resultados de range() diretamente em uma lista usando a função list().

numbers = list(range(1,6))
print(numbers)

#Também podemos usar a função range() para dizer a Python que ignore alguns números em um dado intervalo. Por exemplo, eis o modo de listar os números pares entre 1 e 10:

even_numbers = list(range(2,11,2))#O valor 2 é somado repetidamente até o valor final, que é 11, ser alcançado ou ultrapassado
print(even_numbers)

#Os dez primeiros quadrados perfeitos em uma lista 
squares = []
for value in range(1,11):
  #square = value**2
  squares.append(value**2)

print(squares)

#List comprehensions

squares = [value**2 for value in range(1,11)]
print(squares)

#Estatística simples com lista de números - Algumas funções Python são específicas para listas de números

digits = [1,2,3,4,5,6,7,8,9,0]
print('\nValores da lista:')
print(digits)
print('Valor mínimo: ' + str(min(digits)) + '\nValor máximo: ' + str(max(digits)) + '\nSoma dos números: ' + str(sum(digits)))


