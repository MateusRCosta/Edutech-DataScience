# Criação de Gráficos
# O objetivo é a criação de gráficos de linhas randômicos a partir da biblioteca Matplotlib 

# importando a biblioteca Matplotlib e a função randrange da Biblioteca Random
from matplotlib import pyplot as plt
from random import randrange

# Função que gera valores, determinados pelo usuário
# sendo os valores do Eixo X sequencial começando com 1 e indo até o valor colocado pelo usuário
# e os valores do Eixo Y sendo aleatórios entre o valor máximo e mínimo colocado pelo usuário
def valores(valor_x, valor_min_y, valor_max_y):
    pos_x = list(range(1,valor_x))
    pos_y = [randrange(valor_min_y, valor_max_y) for valor in range(0,valor_x - 1)]
     
    return pos_x, pos_y

# neste exemplo utilizaremos o valor final do Eixo como 7, e os valores de Y, 0 e 100
pos_x, pos_y = valores(7, 0, 100)

# Criação do gráfico
plt.plot(pos_x, pos_y, marker='o')
plt.title('Gráfico Randômico')
plt.xlabel('Eixo X (1, 6)')
plt.ylabel('Eixo Y (0, 100)')
plt.show()
