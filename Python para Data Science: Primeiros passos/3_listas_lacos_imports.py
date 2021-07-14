# Criação de lista, laços e utilização de bibliotecas 
# O objetivo do algoritmo é gerar números aleatórios referente a idade, e a partir deles dizer se é maior de idade ou não.
# OBS : a idade de referência para a maioridade é de 18 anos.

# importando uma função específica da biblioteca random.
from random import randrange

# criação de uma lista vazia para guardar as idades geradas posteriormente
idades = []

# criação de um laço para preencher a lista criada a partir da função randrange retirada da biblioteca random
for idade in range(1,5):
  idades.append(randrange(0, 118))

# criação de um laço para definir quais idades são consideradas maiores de 18 anos e apresentar na tela do usuário
for idade in idades:
  if(idade < 18):
    print('{} anos e é menor de idade.'.format(idade))
  else:
    print('{} anos e é maior de idade.'.format(idade))
