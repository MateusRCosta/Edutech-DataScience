# Criação de Arrays
# O objetivo deste código é mostrar a criação de Arrays Numpy de várias formas possívei

# Importando a biblioteca
import numpy as np

# Array - Numpy
print('Criação de Arrays a partir do Numpy\n\n')

 # Criação de arrays a partir do Numpy
num_pares_np = np.arange(0, 31, 2)
print('Array Numpy de números pares de 0 a 30\n', num_pares_np)
  
 # Conversão de lista Python para Array Numpy
lista_0 = [num for num in range(0, 16)]
lista_np = np.array(lista_0)
 # Conversão de tupla Python para Array Numpy
tupla_py = 12, 213, 1, 76, 812, 12
tupla_np = np.array(a) 
print('\n\nConversão de Lista e Tupla Python para Array Numpy\n\nLista Convertida', lista_np,'\n\nTupla Convertida',tupla_np)

 # Criando Arrays a partir de dados externos 
idade_carro = np.loadtxt(fname = 'carros-anos.txt', dtype = int)
km_carro = np.loadtxt(fname = 'carros-km.txt', dtype = int)
print('\n\n Criação de Arrays Numpy a partir de dados externos\n\n Quilometragem de Carros\n',km_carro,'\n\nIdade de Carros\n',idade_carro)

 # Criação de Arrays de duas Dimensões
dados = np.array([idade_carro, km_carro])
print('\n\n Criação de Array de Duas Dimensões\n', dados)
