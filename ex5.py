# Importe a biblioteca NumPy e crie um array NumPy de números inteiros de 1 a 10.

import numpy as np 

array_inteiros = np.arange(1, 11)
print(array_inteiros)
# Crie um array Numpy de números float aleatórios entre 0 e 1 nas seguintes dimensões 300 x  200 x 3

array_aleatorio = np.random.rand(300, 200, 3)
print(array_aleatorio)
# Crie um array de duas dimensões para guardar notas de alunos de uma disciplina, sendo que existem 20 alunos na sala e cada aluno possuirá 3 notas na disciplina. O array deverá conter números aleatórios inteiros entre 1 e 10 (inclusive)

notas_alunos = np.random.randint(1, 11, size=(20, 3))
print(notas_alunos)
# Crie um array NumPy com 12 elementos e o redimensione em uma matriz 3x4. Em seguida, realize a transposição dessa matriz.

array_original = np.arange(1, 13).reshape(3, 4)

print(f"array originak 3x4 {array_original}")

array_transposto = array_original.T
print(f"array transposto {array_transposto}")

# Crie dois arrays NumPy de mesma forma e realize as quatro operações aritméticas básicas (+, -, *, /) entre eles.

array1 = np.random.randint(1, 10, size=(3,3))
array2 = np.random.randint(1, 10, size=(3,3))

soma = array1 + array2
print(f"Soma: {soma}")
subtracao = array1 - array2
print(f"Subtração: {subtracao}")
mult = array1 * array2
print(f"Multiplicação: {mult}")
div = array1 / array2 
print(f"Divisão: {div}")
# Crie um array NumPy de números de 1 a 20 e, em seguida, imprima os elementos pares utilizando indexação e fatiamento.

array_numeros = np.arange(1, 21)
pares = array_numeros[array_numeros % 2 == 0]
print(f"Pares: {pares}")
# Crie um array NumPy de números aleatórios entre 1 e 100. Em seguida, selecione e exiba apenas os números maiores que 50.

array_aleato = np.random.randint(1, 101, size=20)
maiores_50 = array_aleato[array_aleato > 50]
print("Números maiores que 50:\n", maiores_50)
# Crie um array NumPy com 10 números aleatórios e calcule a média, mediana e desvio padrão desses números.



array_alea = np.random.rand(10)

media = np.mean(array_alea)
mediana = np.median(array_alea)
desvio_padrao = np.std(array_alea)

print("Média:", media)
print("Mediana:", mediana)
print("Desvio padrão:", desvio_padrao)