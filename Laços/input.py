#A função input() faz uma pausa em seu programa e espera o usuário fornecer um texto. Despois que o Python recebe a entrada de usuário, o dado é armazenado em uma variável. 

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# As vezes você vai querer escrever um prompt maior que uma linha. Você pode armazenar seu prompt em uma variável e passá-la para a função input() clara. Exemplo: 

prompt = "If you tell us who you are, we can personalize the messages you see. "
prompt += "\nWhat is your first name? "

name = input(prompt)

# Usando int() para aceitar entradas numéricas 
# Se usarmos input() o Python interpretará o conteúdo como uma String. 
# Usando a função int() diz a Python para tratar a entrada string como um número inteiro. 

age = input("How old are you? ")
print(type(age))

print("Convertendo para inteiro: ")

age = int(age)
print(type(age))

print("\n---Rollercoaster---")
height = input("Qual a sua altura em centímetros: ")
height = int(height)

if (height >= 93):
    print("\nVocê tem a altura necessária para entrar!")
else: 
    print("\nVocê não tem a altura mínima para entrar!")


# O operador de módulo efetua a divisão entre dois números e retorna o resto. 
# Quando um número é divisível por outro, o resto é 0. Podemos utilizar essa informação para saber se um número é par ou é impar.
print("\n---Operador de módulo---")

number = input("Entre com um número e veremos se ele é impar ou par: ")
number = int(number)

if(number % 2 == 0):
    print("\nO número " + str(number) + " é par!")
else: 
    print("\nO número " + str(number) + " é ímpar!")








