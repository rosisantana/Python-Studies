# Números favoritos: Modifique o seu programa do Exercício dicionário1_ex1 para que cada pessoa possa ter mais de um número favorito. Em seguida, apresente o nome de cada pessoa, juntamente com seus números favoritos.

numeros_favoritos = {
  'jake': [9, 5, 4],
  'amy': [2],
  'rosa': [4, 5],
  'charles': [13]
}

for nome, numeros in numeros_favoritos.items():
    if len(numeros) <= 1:
        print('\nO número favorito do(a) ' + nome.title() + ' é: ')
        for numero in numeros:
            print('\t' + str(numero))
    else:
        print('\nOs números favoritos do(a) ' + nome.title() + ' são: ')
        for numero in numeros:
            print('\t' + str(numero))