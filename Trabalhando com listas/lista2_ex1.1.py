#Contando até vinte: Use um laço for para exibir os números de 1 a 20, incluindo-os.

for value in range(1,21):
  print(value)

#Um milhão: Crie uma lista de números de um a um milhão e, então, use um laço for para exibir os números. (Se a saída estiver demorando demais, interrompa pressionando CTRL -C ou feche a janela de saída.)

#Somando um milhão: Crie uma lista de números de um a um milhão e, em seguida, use min() e max() para garantir que sua lista realmente começa em um e termina em um milhão. Além disso, utilize a função sum() para ver a rapidez com que Python é capaz de somar um milhão de números.

super_list = list(range(1,1000001))
print(super_list)
print('Número Mínimo = ' + str(min(super_list)))
print('Número Máximo = ' + str(max(super_list)))
print('Soma = ' + str(sum(super_list)))

#Números ímpares: Use o terceiro argumento da função range() para criar uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos os números.

impares = list(range(1,20,2))
for impar in impares:
  print(impar)

#Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para exibir os números de sua lista.

tres = []
for value in range(1,11):
  tres.append(value*3)
print(tres)

#Cubos: Um número elevado à terceira potência é chamado de cubo. Por exemplo, o cubo de 2 é escrito como 2**3 em Python. Crie uma lista dos dez primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for para exibir o valor de cada cubo.

cubos = []
for value in range(1,11):
  cubos.append(value ** 3)

for cubo in cubos:
  print(cubo)

#Comprehension de cubos: Use uma list comprehension para gerar uma lista dos dez primeiros cubos.

cubos = [value ** 3 for value in range(1,11)]
print(cubos)

