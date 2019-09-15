#Percorrendo uma lista 

#Quando quiser executar a mesma ação em todos os itens de uma lista, você pode usar o laço for de Python.

magicians = ['alice', 'david', 'carolina']
for magician in magicians: #essa linha diz a Python para extrair um nome da lista magicians e armazená-lo na variável magician
  print(magician)

#Executando mais tarefas com o laço for
magicians = ['alice', 'david', 'carolina']
for magician in magicians: 
  print(magician.title() +", that was a great trick!")
  print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")

