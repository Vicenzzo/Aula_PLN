import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Carregar o arquivo para leitura e gerar listas
file_path = 'weatherAUS.csv'  # Caminho do arquivo CSV contendo os dados do clima
temperatura_minima = []  # Lista para armazenar as temperaturas mínimas
temperatura_maxima = []  # Lista para armazenar as temperaturas máximas
chuva = []  # Lista para armazenar a ocorrência de chuva (1=Sim, 0=Não)

# Abrir o arquivo e processar linha por linha
with open(file_path, 'r') as file:
    header = file.readline().strip().split(',')  # Ler o cabeçalho e identificar os índices das colunas
    for line in file:
        data = line.strip().split(',')  # Dividir os valores da linha atual por vírgula
        try:
            # Obter os valores das colunas de interesse
            temp_min = float(data[header.index('MinTemp')])  # Temperatura mínima
            temp_max = float(data[header.index('MaxTemp')])  # Temperatura máxima
            rainfall = float(data[header.index('Rainfall')])  # Quantidade de chuva

            # Adicionar os valores às listas correspondentes
            temperatura_minima.append(temp_min)
            temperatura_maxima.append(temp_max)
            chuva.append(1 if rainfall > 0 else 0)  # Converter chuva em binário (1=Choveu, 0=Não choveu)
        except (ValueError, IndexError):  # Ignorar linhas com dados ausentes ou inválidos
            continue  

# 2. Transformar as listas em arrays do NumPy
X = np.array(list(zip(temperatura_minima, temperatura_maxima)))  # Criar matriz de variáveis independentes (X)
y = np.array(chuva)  # Vetor com o alvo (y), indicando chuva ou não

# 3. Separar o conjunto de dados entre treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)  # Dividir os dados em 70% para treino e 30% para teste

# 4. Criar o modelo de Regressão Logística
model = LogisticRegression()  # Instanciar o modelo de regressão logística

# 5. Treinar o modelo com os dados de treinamento
model.fit(X_train, y_train)  # Ajustar o modelo com os dados de treino

# 6. Verificar o Score do modelo
score = model.score(X_test, y_test)  # Avaliar o modelo usando o conjunto de teste
print(f'Acurácia do modelo: {score:.2f}')  # Exibir a acurácia do modelo

# 7. Gerar alguns valores para fazer a predição
predictions = model.predict(X_test)  # Fazer predições com o conjunto de teste

# 8. Escolher um dos features e plotar
plt.figure(figsize=(10, 6))  # Configurar o tamanho do gráfico
plt.scatter(
    X_test[:, 0], predictions, color='blue', alpha=0.5, label='Predição de Chuva'
)  # Plotar as predições baseadas na temperatura mínima
plt.scatter(
    X_test[:, 0], y_test, color='red', alpha=0.5, label='Dados Reais'
)  # Plotar os valores reais de chuva baseados na temperatura mínima
plt.title('Predição de Chuva com Temperatura Mínima')  # Título do gráfico
plt.xlabel('Temperatura Mínima (°C)')  # Rótulo do eixo X
plt.ylabel('Chuva (1=Sim, 0=Não)')  # Rótulo do eixo Y
plt.legend()  # Adicionar legenda
plt.grid()  # Adicionar grade ao gráfico
plt.show()  # Mostrar o gráfico
