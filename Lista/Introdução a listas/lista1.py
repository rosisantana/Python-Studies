#A lista é uma coleção de itens em uma ordem particular. Em Python, colchetes([]) indicam uma lista, e os elementos individuais são separados por vírgulas.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Para acessar os elementos qualquer elemento individual de uma lista, basta informar a sua posição (ou índice). Exemplo:

print('\nAcessando o elemento indivdual de índice [0]: ' + bicycles[0].title())

#Para acessar o útimo índice da lista, basta solicitar o índice -1. O índice -2 devolve o segundo item a partir do final da lista, o índice -3 devolve o terceiro item a partir do final, e assim sucessivamente.

print('\nAcessando o último elemento, índice [-1]: ' + bicycles[-1].title())

message = 'My first bicycle was a ' + bicycles[0].title() +'.'
print('\nUsando o método title() com lista: ' + message)
