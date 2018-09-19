# Implementação da técnica de treinamento de redes neurais ADALINE NEURAL NETWORK


# Prof Keiji Yamanaka

from random import uniform
#from pyplot import matplotlib as pl
import matplotlib.pyplot as plt

# Inputs
x = [[1,1],
    [1,1],
    [1,-1],
    [-1,-1]]

# Parametros
t = [1,-1, -1, -1]              # Target
alfa = 0.2                      # Taxa de aprendizagem
teta = 0                        # Limiar de ativação
# Criterios de parada
erroAceitavel = 0.01            # Flag de erro da rede neural
cicloMax = 100
tolerancia = 0.0001             # Ajuste maximo admissivel dos pesos

# Inicialização dos pesos
Wanterior = []
for i in range(2):
    Wanterior.append(uniform(-0.5,0.5))    # Vetor de 1 linha e duas colunas
Banterior = uniform(-0.5, 0.5)             # Um escalar
Yin = 0.0
Wnovo = Wanterior
Bnovo = Banterior

ciclos = 0
while (ciclos < cicloMax):
    ciclos = ciclos +1
    EqTotal = 0                     # Erro Quadratico total
    # Inserir padrões de treinamento
    for padrao in range(4):
        EqTotal = EqTotal + 0.5 * (t[padrao] - Yin)**2
        # Atualização dos pesos
        Bnovo = Banterior + alfa * (t[padrao] - Yin)
        for k in range(2):
            Wnovo[k] = Wanterior[k] + alfa * x[padrao][k] * (t[padrao]- Yin)
            Yin = Banterior + x[padrao][k]*Wanterior[k]
        Wanterior = Wnovo
        Banterior = Bnovo
        
    #pl(ciclos, EqTotal)
    
print(Wanterior)
print(Banterior)
print('CICLOS: ',ciclos)

"""
    Tarefa: Colocar a tolerancia como critério de parada

    -------
    MELHORAR MEU CÓDIGO

"""
"""


def error( ):

    return 

def 
"""