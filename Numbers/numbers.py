#Erros de tipo com a função str(): Ao usar inteiros em strings, é preciso especificar explicitamente que quer que Python utilize o inteiro como uma string de caracteres. Utilizamos a função str()

age = 23 
message = 'Happy ' + str(age) + 'rd Birthday'
print(message)