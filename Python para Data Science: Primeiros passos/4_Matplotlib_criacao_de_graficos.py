# Criação de Gráficos
# O objetivo é a criação de gráficos de linhas randômicos a partir da biblioteca Matplotlib 

# importando a biblioteca Matplotlib e a função randrange da Biblioteca Random
from matplotlib import pyplot as plt
from random import randrange

# Função que gera valores, sendo o eixo X valores sequenciais de 1 a 6 
# e o Eixo Y valores aleatórios entre 0 a 100
def valores():
    pos_x = list(range(1,7))
    pos_y = [randrange(0, 100) for valor in range(0,6)]
     
    return pos_x, pos_y
 
pos_x, pos_y = valores()

# Criação do gráfico
plt.plot(pos_x, pos_y, marker='o')
plt.title('Gráfico Randômico')
plt.xlabel('Eixo X (1, 6)')
plt.ylabel('Eixo Y (0, 100)')
plt.show()
