import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Carregar o arquivo para leitura e gerar listas
file_path = 'heart.csv'  # Caminho do arquivo CSV contendo os dados sobre saúde cardíaca
age = []  # Lista para armazenar as idades
sex = []  # Lista para armazenar os sexos
cp = []  # Lista para armazenar os tipos de dor no peito
trtbps = []  # Lista para armazenar a pressão arterial em repouso
chol = []  # Lista para armazenar os valores de colesterol
fbs = []  # Lista para armazenar o nível de açúcar no sangue em jejum
target = []  # Lista para armazenar o alvo (ataque cardíaco: 0 = Não, 1 = Sim)

# Ler o arquivo CSV
with open(file_path, 'r') as file:
    header = file.readline().strip().split(',')  # Ler o cabeçalho e identificar os índices das colunas
    for line in file:
        data = line.strip().split(',')  # Dividir os valores da linha atual por vírgula
        try:
            # Preencher as listas com os valores das colunas correspondentes
            age.append(int(data[0]))  # Idade
            sex.append(int(data[1]))  # Sexo (0 = Feminino, 1 = Masculino)
            cp.append(int(data[2]))  # Tipo de dor no peito
            trtbps.append(float(data[3]))  # Pressão arterial em repouso
            chol.append(float(data[4]))  # Colesterol
            fbs.append(int(data[5]))  # Açúcar no sangue em jejum (>120 mg/dl: 1, caso contrário: 0)
            target.append(int(data[13]))  # Alvo: ataque cardíaco (0 = Não, 1 = Sim)
        except (ValueError, IndexError):  # Ignorar linhas com dados inválidos ou incompletos
            continue 

# 2. Transformar as listas em arrays do NumPy
X = np.array(list(zip(age, sex, cp, trtbps, chol, fbs)))  # Matriz de variáveis independentes
y = np.array(target)  # Vetor com os alvos (ataque cardíaco)

# 3. Separar o conjunto de dados entre treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)  # Dividir os dados em 80% para treino e 20% para teste

# 4. Criar o modelo de Regressão Logística
model = LogisticRegression(max_iter=200)  # Instanciar o modelo com um limite de 200 iterações

# 5. Treinar o modelo com os dados de treinamento
model.fit(X_train, y_train)  # Ajustar o modelo com os dados de treino

# 6. Verificar o Score do modelo
score = model.score(X_test, y_test)  # Avaliar o modelo usando o conjunto de teste
print(f'Acurácia do modelo: {score:.2f}')  # Exibir a acurácia do modelo

# 7. Gerar alguns valores para fazer a predição
predictions = model.predict(X_test)  # Fazer predições com o conjunto de teste

# 8. Escolher um dos features e plotar
plt.figure(figsize=(10, 6))  # Configurar o tamanho do gráfico

# Escolher a idade como feature para plotagem
plt.scatter(X_test[:, 0], predictions, color='b', alpha=0.5, label='Predições')  # Plotar as predições baseadas na idade
plt.scatter(X_test[:, 0], y_test, color='r', alpha=0.3, label='Dados Reais')  # Plotar os valores reais baseados na idade

plt.title('Predição de Ataque Cardíaco com Idade', fontsize=16)  # Título do gráfico
plt.xlabel('Idade', fontsize=14)  # Rótulo do eixo X
plt.ylabel('Predição de Ataque Cardíaco (0 = Não, 1 = Sim)', fontsize=14)  # Rótulo do eixo Y
plt.legend()  # Adicionar legenda ao gráfico
plt.grid()  # Adicionar grade ao gráfico
plt.show()  # Exibir o gráfico
