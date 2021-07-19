# Criação de funções com paramêtros e utilização de condicionais
# Objetivo do algoritmo é receber uma idade e um nome colocado pelo usuário e dizer se este pode tirar uma licença de motorista.
# OBS: A idade de referência para tirar a licença de motorista é de 18 anos

# definindo uma função que retornará o nome e a idade digitado pelo usuário
def questionario():
  nome_questionario = str(input('Digite seu nome:')).strip()
  idade_questionario = int(input('\nDigite sua idade: '))
  return nome_questionario, idade_questionario
          
# criando uma função com paramêtros
def habilitacao(nome_habilitacao, idade_habilitacao):
  
  #criação da condicional                        
  if(idade < 18):
    print('Olá {}, você possui {} anos e não pode tirar a licença de motorista'.format(nome_habilitacao, idade_habilitacao))
  else:
    print('Olá {}, você possui {} anos e pode tirar a licença de motorista'.format(nome_habilitacao, idade_habilitacao))

# executando as funções criadas
nome, idade = questionario()           
habilitacao(nome, idade)
             
