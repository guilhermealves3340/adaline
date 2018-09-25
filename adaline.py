# Implementação da técnica de treinamento de redes neurais ADALINE

# Prof Keiji Yamanaka

# Colocando criterio de parada como tolerancia maior que 0.0001 por exemplo

from random import uniform
import matplotlib.pyplot as plt
import math

x = [[1, 1], [-1, 1], [1, -1], [-1, -1]]        # Inputs

t = [1, -1, -1, -1]             # Target
# Parametros
alfa = 0.12                     # Taxa de aprendizagem
EqAdmissivel = 0.01             # Erro quadratico total
CicloMax = 100                  # Limite de ciclo
tolerancia = 0.0001             # Ajuste maximo admissivel dos pesos


# Inicialização dos pesos entre -0.5 e 0.5
Wanterior = [0, 0]
for i in range(2):
    Wanterior[i] = (uniform(-0.5, 0.5))    # Vetor de 1 linha e duas colunas

Banterior = uniform(-0.5, 0.5)                        # Um escalar
Wnovo = Wanterior
Bnovo = Banterior

# Treinamento da rede neural
ciclos = 0
matriz = [[], []]
r = 1
sinal = True
while sinal:
    ciclos = ciclos + 1
    EqTotal = 0                             # Erro quadratico total
    
    # Inserindo padroes de treino
    for padrao in range(4):
        Yin = Banterior + (x[padrao][0] * Wanterior[0]) + (x[padrao][1] * Wanterior[1])
        EqTotal = EqTotal + (0.5 * ((t[padrao] - Yin)**2))

        # Atualização dos pesos
        r = Banterior
        Bnovo = Banterior + (alfa * (t[padrao] - Yin))
        r = Bnovo - r
        if math.sqrt(r**2) < math.sqrt(tolerancia**2):
            sinal = False
            break

        for i in range(2):
            r = Wanterior[i]
            Wnovo[i] = Wanterior[i] + (alfa * x[padrao][i] * (t[padrao] - Yin))
            r = Wnovo[i] - r
            if math.sqrt(r**2) < math.sqrt(tolerancia**2):
                sinal = False
                break

        if sinal == False:
            break
        Wanterior = Wnovo
        Banterior = Bnovo
    
    print(r*-1)
    print('CICLOS: ',ciclos)
    print('\n')
    #print(EqTotal)
    #print(Yin)                         # Printando as entradas
    matriz[0].append(ciclos)
    matriz[1].append(EqTotal)

j = 1
for i in Wanterior:
    print('w', j, ' -> ', i)
    j += 1
print('b -> ', Banterior)
print('CICLOS: ', ciclos)
plt.plot(matriz[0], matriz[1], 'ro')
plt.axis([0, 100, 0, 2])
plt.show()
