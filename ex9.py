import numpy as np
import matplotlib.pyplot as plt

np.random.seed(50)
desvio = np.random.random(size=10) * 0.10
desvio

mm_chuva = np.arange(50, 150, 10)
mm_chuva
mm_chuva = mm_chuva * desvio
mm_chuva


colheita = np.arange(3, 103, 10)
colheita = colheita * desvio
colheita

x = mm_chuva
y = colheita

def equacao_linear(x, w, b):
    return (x * w) + b
    
def calcular_custo(y, y_hat):
    qtd_pontos = len(y)  # m
    custo = (y_hat - y) ** 2 
    return np.sum(custo) / (qtd_pontos * 2)

for w n range(0, 10, 0.1):
    b = -1
    w = 0.7
    y_hat = equacao_linear(x, w, b)
    calcular_custo(y, y_hat)
    

plt.scatter(x, y)
plt.plot(x, y_hat, color="red")
plt.xlabel("MM Chuva")
plt.ylabel("Toneladas de Colheita")
plt.show()