""" A empresa BomTempo possui um conjunto de dados meteorológicos contendo a temperatura média diária da cidade Praça Comprida ao longo de um ano.

Exercício: Com base no conjunto de dados meteorológicos abaixo, utilize o NumPy para calcular as seguintes informações:

· temperatura média anual

· temperatura máxima registrada

· temperatura mínima registrada

· desvio padrão da temperatura
"""

import numpy as np
dados_meteorologicos = [25, 26, 27, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12]

dados_np_meteorologicos = np.array(dados_meteorologicos)
print(dados_np_meteorologicos)

media = np.mean(dados_np_meteorologicos)
print(f'Temperatura média anual: {media}°C')
maxima = np.max(dados_np_meteorologicos)
print(f'Temperatura máxima registrada: {maxima}°C')
minima = np.min(dados_np_meteorologicos)
print(f'Temperatura mínima registrada: {minima}°C')
desvio_padrao = np.std(dados_np_meteorologicos)
print(f'Desvio padrão da temperatura: {desvio_padrao}°C')
