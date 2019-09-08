'''Erros de tipo com a função str(). Quando usar inteiros em strings, é preciso especificar explicitamente que quer que Phython utilize o inteiro como uma string de caracteres. Fazemos com a função str()'''

age = 23 
message = 'Happy ' + str(age) + 'rd Birthday'
print(message)