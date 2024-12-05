import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

# Gerar um array de desvios aleatórios (valores entre 0 e 1)
desvio = np.random.random(size=100)

# Criar um array de valores de milímetros de chuva (50 a 150)
milimetros_chuva = np.arange(50, 150)

# Ajustar os valores de milímetros de chuva aplicando uma pequena variação (10%)
milimetros_chuva *= (desvio * 0.10)

# Criar um array de valores de colheita (3 a 103)
colheita = np.arange(3, 103)

# Ajustar os valores de colheita aplicando a mesma variação de 10%
colheita *= (desvio * 0.10)

# Redimensionar o array de milímetros de chuva para uma matriz de 2 dimensões
# (necessário para o modelo de regressão)
milimetros_chuva = milimetros_chuva.reshape(-1, 1)

# Inicializar o modelo de regressão linear
modelo_regressao = LinearRegression()

# Treinar o modelo com os dados (milímetros de chuva como entrada e colheita como saída)
modelo_regressao.fit(milimetros_chuva, colheita)

# Obter o coeficiente angular (W) e o intercepto (B) do modelo treinado
coeficiente = modelo_regressao.coef_[0]  # Inclinação da reta
intercepto = modelo_regressao.intercept_  # Intercepto da reta

# Fazer previsões de colheita com base nos milímetros de chuva usando o modelo treinado
colheita_prevista = modelo_regressao.predict(milimetros_chuva)

# Imprimir os valores dos coeficientes do modelo
print(f"Melhores valores: W = {coeficiente:.4f}, B = {intercepto:.4f}")

# Plotar os dados reais (dispersão) e a previsão da regressão (reta)
plt.scatter(milimetros_chuva, colheita, label='Dados Reais')  # Gráfico de dispersão para os dados reais
plt.plot(milimetros_chuva, colheita_prevista, color='red', label=f'Previsão (W={coeficiente:.4f}, B={intercepto:.4f})')  # Reta de regressão
plt.xlabel('Milímetros de Chuva')  # Rótulo do eixo X
plt.ylabel('Colheita')  # Rótulo do eixo Y
plt.legend()  # Exibir a legenda do gráfico
plt.show()  # Mostrar o gráfico
