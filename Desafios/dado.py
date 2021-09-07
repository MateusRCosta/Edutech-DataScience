#Importando API
import pandas as pd
from random import randint
from time import sleep

def texto(seg):
  if seg == 0:
    print(f'...\n...\n{dado}')
  
  else:
    seg_1 = seg/2 
    print('...')
    sleep(seg_1)
    print('...')
    sleep(seg_1)
    print(dado)

  
segs = 2
num_dado = []

afirmacao = ['SIM','SS','S']
negacao = ['NAO','NÃO','N','NN']
temporizador = ['TIME','TEMPO']

resposta_jogador = input(str('Gostaria de jogar o dado ?\n:')).upper().strip()

# Estrutura de Laço  

while resposta_jogador in afirmacao or negacao:
    
    if resposta_jogador in afirmacao:
      
      dado = randint(1,6)
      num_dado.append(dado)
      texto(segs)
      resposta_jogador = input(str('Gostaria de continuar a jogar dado ?\n:')).upper().strip()

    elif resposta_jogador in negacao:
      
      if len(num_dado) == 0:
        print('Ok, numa próxima a gente joga =)')
      
      else:
        print('Tudo bem, numa próxima a gente joga mais.\nForam jogados {} vezes'.format(len(num_dado)))
      
      break
    
    elif resposta_jogador in temporizador:
      segs = float(input('Coloque em segundos o tempo para dar a resposta\n:'))
      resposta_jogador = input(str('Gostaria de continuar a jogar dado ?\n:')).upper().strip()
    
    else:
      print('Coloque uma resposta válida:\nNegação:não, nao, nn, n\nConfirmação:sim, ss, s\n "time" ou "tempo" para modificar o tempo de resposta, lembrando que tem que ser em segundos. ')
      resposta_jogador = input(str('Gostaria de jogar o dado ?\n:')).upper().strip()

# Criação de um DataFrame a partir dos dados jogados, tendo como indice as faces do dado e uma coluna com o número de vezes que caiu a face

series_dado = pd.Series(num_dado).value_counts()

df = pd.DataFrame(data = range(1,7),
                  columns = ['a'],
                  index = range(1,7))

info_dado = pd.concat([df, series_dado], axis = 1)
info_dado.columns = ['a','vezes']
del info_dado['a']
info_dado.columns.name ='Face'
info_dado.fillna(0).astype(int)
