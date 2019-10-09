# Locação de automóveis: Escreva um programa que digite o tipo de carro que ele gostaria de alugar. Mostre uma mensagem sobre esse carro, por exemplo: "Deixe-me ver se consigo um Subaru para você!"

carro = input("Qual carro você gostaria de alugar? ")
print("Felizmente, o " + carro + " está disponível!")

# Lugares em um restaurante: Escreva um programa que pergunte ao usuário quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que 8, exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso contrário, informe que a mesa está pronta!

jantar = input("\nQuantas pessoas vão jantar? ")
print("\n..........Verificando se a mesa está pronta............")
jantar = int(jantar)

if (jantar > 8):
    print("\nVocês deverão aguardar por uma mesa!")
else: 
    print("\nA mesa está pronta!")

# Múltiplos de dez: Peça um número ao usuário e, em informe se o número é múltiplo de 10. 

numero = input("\nInforme um número: ")
numero = int(numero)

if (numero % 10 == 0):
    print("O número "+ str(numero) +" é um múltiplo de 10!")
else : 
    print("O número "+ str(numero) +" é um múltiplo de 10!")



