import numpy as np
import matplotlib.pyplot as plt

# 1. Carregar o arquivo e gerar listas
anos = []  # Lista para armazenar os anos
populacao_urbana = []  # Lista para armazenar a população urbana

# Abrir o arquivo CSV com os dados de população urbana
arquivo = open('population.csv', 'r', encoding='utf-8')
texto = " "  # Variável temporária para leitura de linhas
contador = 0  # Contador para rastrear a linha atual

while texto != '':  # Loop até que todas as linhas sejam lidas
    texto = arquivo.readline()  # Ler uma linha do arquivo
    if contador > 0 and texto != '':  # Ignorar o cabeçalho e linhas vazias
        data = texto.strip().split(',')  # Dividir os dados separados por vírgulas
        try:
            anos.append(int(data[0]))  # Adicionar o ano à lista
            populacao_urbana.append(float(data[8]))  # Adicionar a população urbana à lista
        except ValueError as e:  # Tratar erros de conversão
            print(f"Erro ao processar a linha: {texto.strip()}. Erro: {e}")
    contador += 1  # Incrementar o contador de linhas

arquivo.close()  # Fechar o arquivo após a leitura

# 2. Transformar listas em arrays do NumPy para facilitar cálculos matemáticos
x = np.array(anos)  # Converter lista de anos em array do NumPy
y = np.array(populacao_urbana)  # Converter lista de população urbana em array do NumPy

# 3. Declarar a função linear que será usada para modelar os dados
def funcao_linear(x, w, b):
    return w * x + b  # Retorna o valor previsto pela equação linear y = wx + b

# 4. Escolher valores iniciais para os parâmetros w (inclinação) e b (intercepto)
w = 0.1  # Valor inicial para o peso (inclinação)
b = 2  # Valor inicial para o intercepto

# Calcular os valores previstos y_hat com os parâmetros iniciais
y_hat = funcao_linear(x, w, b)

# 5. Plotar os dados reais e a linha de regressão inicial
plt.scatter(x, y, color='blue', label='Dados Reais')  # Gráfico de dispersão dos dados reais
plt.plot(x, y_hat, color='red', label='Linha de Regressão')  # Linha de regressão inicial
plt.xlabel('Ano')  # Rótulo do eixo X
plt.ylabel('População Urbana')  # Rótulo do eixo Y
plt.title('População Urbana da Índia ao longo dos Anos')  # Título do gráfico
plt.legend()  # Exibir legenda
plt.show()  # Mostrar o gráfico

# 6. Criar a função de custo (função de erro) para avaliar a qualidade do modelo
def custo(y, y_hat):
    m = len(y)  # Número de exemplos
    return np.sum((y_hat - y) ** 2) / (2 * m)  # Retorna o custo médio quadrático

# 7. Executar a função de custo com os valores iniciais de w e b
custo_atual = custo(y, y_hat)
print(f'Custo atual: {custo_atual}')  # Exibir o custo inicial

# 8. Criar a função novo_w para atualizar o peso w com base no gradiente descendente
def novo_w(w, x, y, y_hat, learn_rate):
    m = len(y)  # Número de exemplos
    gradiente = np.sum((y_hat - y) * x) / m  # Gradiente da função de custo em relação a w
    return w - learn_rate * gradiente  # Atualizar w com o gradiente

# 9. Criar a função novo_b para atualizar o intercepto b com base no gradiente descendente
def novo_b(b, x, y, y_hat, learn_rate):
    m = len(y)  # Número de exemplos
    gradiente = np.sum(y_hat - y) / m  # Gradiente da função de custo em relação a b
    return b - learn_rate * gradiente  # Atualizar b com o gradiente

# 10. Executar o treinamento do modelo por 30 iterações
learn_rate = 0.01  # Taxa de aprendizado para o gradiente descendente

for _ in range(30):  # Loop para realizar 30 iterações de treinamento
    y_hat = funcao_linear(x, w, b)  # Calcular os valores previstos com os parâmetros atuais

    custo_atual = custo(y, y_hat)  # Calcular o custo atual com os valores previstos

    w = novo_w(w, x, y, y_hat, learn_rate)  # Atualizar w usando a função de gradiente
    b = novo_b(b, x, y, y_hat, learn_rate)  # Atualizar b usando a função de gradiente

    print(f'W: {w}, B: {b}, Custo atual: {custo_atual}')  # Exibir os valores atualizados de w, b e custo

# 11. Plotar os dados reais e a linha de regressão otimizada
y_hat_otimizado = funcao_linear(x, w, b)  # Calcular os valores previstos com os parâmetros otimizados

plt.scatter(x, y, color='blue', label='Dados Reais')  # Gráfico de dispersão dos dados reais
plt.plot(x, y_hat_otimizado, color='green', label='Linha de Regressão Otimizada')  # Linha de regressão final
plt.xlabel('Ano')  # Rótulo do eixo X
plt.ylabel('População Urbana')  # Rótulo do eixo Y
plt.title('População Urbana da Índia ao longo dos Anos (Otimizada)')  # Título do gráfico
plt.legend()  # Exibir legenda
plt.show()  # Mostrar o gráfico final
