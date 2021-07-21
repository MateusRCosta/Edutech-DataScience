# Operações com Array 
# O objetivo deste código é mostrar operações matemáticas com o Array 

# Importando a Biblioteca
import numpy as np 

# Criando os dados que serão utilizados
km = [44410., 5712., 37123., 0., 25757.]
anos = [2003, 1991, 1990, 2019, 2006]

km_np = np.array(km)
anos_np = np.array(anos)

# Operações entre Arrays e Constantes 
print('-> Operações entre Arrays e Constantes\n\nIdade de Veículos\n\n') 

 # Sem Numpy 
idades_carros_py = []
for x in anos:
  idade = 2021 - x
  idades_carros_py.append(idade)
print('*Sem Numpy',idades_carros_py)
 
 # Com Numpy
anos_np = np.array(anos)
idade_carros = 2021 - anos_np
print('\n\n*Com Numpy', idade_carros )

# Operações entre Arrays
print('\n\n -> Operações entre Arrays\n\nQuilometragem média Anual\n\n')

 # Sem Numpy
km_media_py = []       
for roda in km:
  km_media_py_1 = roda / idade
  km_media_py.append(km_media_py_1)
print('*Sem Numpy',km_media_py)
 
  # Com Numpy 
km_media_np = km_np / (2021 - anos_np)
print('\n\n*Com Numpy',km_media_np)

# Operação com array de duas Dimensões
print('\n\n Operação com array de duas Dimensões -- Quilometragem Média Anual\n\n')
dados = np.array([anos_np, km_np])
km_media_np_dd = dados[1] / (2021 - dados[0]) 
print(km_media_np_dd)
