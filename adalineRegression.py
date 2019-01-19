"""
    Trabalho: implementar um Adaline que realize a
    regressão linear para os dados abaixo.

    - Comparar com os obtidos utilizando as equações de a e 
    b.

    - Encontrar coeficiente de correlação de Pearson e o
    coeficiente de determinação
"""
import matplotlib.pyplot as plt
from random import uniform

# Inputs
x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]                                 # Eixo x

# Target
y = [2.26, 3.8, 4.43, 5.91, 6.18, 7.26, 8.15, 9.14, 10.87, 11.58, 12.55]        # Eixo y

# Parametros
alfa = 0.0012
cicloMax = 1000
tolerancia = 0.0001
EqAdmissivel = 0.47

# Inicialização dos pesos entre -0.5 e 0.5

Wanterior = uniform(-0.5, 0.5)
Banterior = uniform(-0.5, 0.5)
Wnovo = Wanterior
Bnovo = Banterior

# Treinando a rede neural
ciclos = 0
matriz=[[],[]]
EqTotal = 1
while EqTotal > EqAdmissivel:
    ciclos = ciclos +1
    EqTotal = 0

    # Inserindo padroes de treino
    for i in range(len(x)):
        Yin = Banterior + (x[i] * Wanterior)
        EqTotal = EqTotal + (0.5 * ( y[i]-Yin)**2)  # Expressão ERRO QUADRATICO

        # Atualização dos pesos
        Bnovo = Banterior + (alfa * (y[i] - Yin))

        Wnovo = Wanterior + (alfa * x[i] * (y[i] - Yin))

        Wanterior = Wnovo
        Banterior = Bnovo
    
    print(EqTotal)

    matriz[0].append(ciclos)
    matriz[1].append(EqTotal)
 
print('w', ' -> ', Wanterior)
print('b -> ', Banterior)
print('CICLOS: ', ciclos)
plt.plot(matriz[0], matriz[1], 'ro')
plt.axis([0, 80, 0, 60])
plt.show()

"""
plt.plot(x, y, 'ro')
plt.axis([0,15, 0,30])
plt.show()

"""

"""
    Tarefa
    -------
    Treinar adaline para reconhecer dígitos
"""