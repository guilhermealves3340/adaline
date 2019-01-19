"""
    ANOTAÇÕES DE AULA:
    MARVIIN MINSKY

    fazer relatório do trab 05(condição de parada como erro)

    Eqtotal x cilos : plot
"""

import matplotlib.pyplot as plt
from random import uniform

# Target    (Matriz identidade de target)
t0 = [+1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
t1 = [-1,+1,-1,-1,-1,-1,-1,-1,-1,-1]
t2 = [-1,-1,+1,-1,-1,-1,-1,-1,-1,-1]
t3 = [-1,-1,-1,+1,-1,-1,-1,-1,-1,-1]
t4 = [-1,-1,-1,-1,+1,-1,-1,-1,-1,-1]
t5 = [-1,-1,-1,-1,-1,+1,-1,-1,-1,-1]
t6 = [-1,-1,-1,-1,-1,-1,+1,-1,-1,-1]
t7 = [-1,-1,-1,-1,-1,-1,-1,+1,-1,-1]
t8 = [-1,-1,-1,-1,-1,-1,-1,-1,+1,-1]
t9 = [-1,-1,-1,-1,-1,-1,-1,-1,-1,+1]

t = [t0,t1,t2,t3,t4,t5,t6,t7,t8,t9]

# Parametros
alfa = 0.0012
cicloMax = 1000
tolerancia = 0.0001
EqAdmissivel = 0.47

# Inicialização dos pesos entre -0.5 e 0.5
Banterior = uniform(-0.5, 0.5)
Bnovo = Banterior



