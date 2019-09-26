# Pessoa: Use um dicionário para armazenar informações sobre uma pessoa que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a cidade em que ela vive. Você deverá ter chaves como first_name, last_name, age e city. Mostre cada informação armazenada em seu dicionário. 

usuario = {
  'primeiro_nome': 'rosimeire',
  'sobrenome': 'santana',
  'idade': 24,
  'cidade': 'santo andré'
}

print(usuario, '\n')

# Números favoritos: Use um dicionário para armazenar os números favoritos de algumas pessoas. Pense em cinco nomes e use-os como chaves em seu dicionário. Pense em um número favorito para cada pessoa e armazene cada um como um valor em seu dicionário. Exiba o nome de cada pessoa e seu número favorito.

numeros_favoritos = {
  'jake': 13,
  'amy': 5,
  'rosa': 6,
}

print('O número favorito do Jake é ' + str(numeros_favoritos['jake']))
print('O numero favorito da Amy é ' + str(numeros_favoritos['amy']))
print('O número favorito da Rosa é ' + str(numeros_favoritos['rosa']))


glossario = { 
  'algoritmo': 'conjunto das regras e procedimentos lógicos perfeitamente definidos que levam à solução de um problema em um número finito de etapas.'
  
}

print('Algoritmo: ' + glossario['algoritmo'])