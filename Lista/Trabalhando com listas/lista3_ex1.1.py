#Faça uma lista e acrescente várias linhas no final do programa que façam o seguinte:
#Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para exibir os três primeiros itens da lista desse programa.

personagens = ['leia organa', 'han solo', 'luke skywalker', 'darth vader', 'chewbacca']

print('Os três primeiros personagens da lista são:')
print(personagens[:3])
print('\n')

#Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir três itens do meio da lista.

print('Os três personagens do meio da lista são:')
print(personagens[1:4])
print('\n')

#Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir os três últimos itens da lista.

print('Os três últimos personagens são:')
print(personagens[-3:])

