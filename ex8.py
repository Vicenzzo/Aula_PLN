import numpy as np

def calcular_pontuacoes(notas, pesos):
    return np.dot(notas, pesos)

def main():
    # Coletar dados principais
    num_alunos = int(input("Informe quantos alunos serão avaliados: "))
    num_secoes = int(input("Informe a quantidade de seções: "))
    
    # Coletar pesos
    pesos = np.array([float(input(f"Peso da seção {i + 1}: ")) for i in range(num_secoes)])
    
    # Verificar se a soma dos pesos é igual a 10.0
    if np.sum(pesos) != 10.0:
        print("A soma dos pesos deve ser igual a 10.0.")
        return

    # Coletar notas dos alunos
    notas = np.array([[float(input(f"Nota da seção {j + 1} do aluno {i + 1}: ")) for j in range(num_secoes)] for i in range(num_alunos)])

    # Calcular e exibir as pontuações finais
    pontuacoes_finais = calcular_pontuacoes(notas, pesos)
    for i, pontuacao in enumerate(pontuacoes_finais, 1):
        print(f"Pontuação final do aluno {i}: {pontuacao:.2f}")

if __name__ == "__main__":
    main()
