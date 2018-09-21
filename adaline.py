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
matriz = [[],[]]
# Parametros
t = [1,-1, -1, -1]              # Target
alfa = 0.01                     # Taxa de aprendizagem
teta = 0                        # Limiar de ativação
# Criterios de parada
erroAceitavel = 0.01            # Flag de erro da rede neural
cicloMax = 100
tolerancia = 0.0001             # Ajuste maximo admissivel dos pesos

# Inicialização dos pesos
Wanterior = []

for i in range (0,1):
    Wanterior.append(uniform(-0.5,0.5))    # Vetor de 1 linha e duas colunas
    
Banterior = uniform(-0.5, 0.5)             # Um escalar
Yin = 0.0                                  # Saída
Wnovo = Wanterior
Bnovo = Banterior
matriz = [[],[]]
ciclos = 0
while (ciclos < cicloMax):
    ciclos = ciclos +1
    EqTotal = 0                     # Erro Quadratico total
    # Inserir padrões de treinamento
    for padrao in range(0,3):
        EqTotal = EqTotal + (0.5 * ((t[padrao] - Yin)**2))
        # Atualização dos pesos
        Bnovo = Banterior + (alfa * (t[padrao] - Yin))
        for k in range(0,1):
            print("sou k " + k)
            Wnovo[k] = Wanterior[k] + (alfa * x[padrao][k] * (t[padrao]- Yin))
            Yin = Banterior + (x[padrao][k]*Wanterior[k])
        Wanterior = Wnovo
        Banterior = Bnovo
    matriz[0].append(ciclos)
    matriz[1].append(EqTotal)
    print(EqTotal)
j=1
for i in Wanterior:
    print('w',j,' -> ', i)
    j = j +1

print('b -> ',Banterior)
print('CICLOS: ',ciclos)
plt.plot(matriz[0],matriz[1],'ro')
plt.axis([0,100,0,2])
plt.show()
"""
    Tarefa: Colocar a tolerancia como critério de parada

    -------
    MELHORAR MEU CÓDIGO

"""
"""
    Modular em funções 
    Usar map()
    Usar numpy para os arrays
    Fazer plot

"""
