texto = """
Python é uma linguagem de programação poderosa e versátil.
É amplamente utilizada em desenvolvimento web, ciência de dados, 
inteligência artificial e muito mais.
"""

pegar_virgula = texto.find(",")

pegar_ponto = texto.find(".")

texto_novo = ""

for t in range(pegar_ponto + 1, pegar_virgula): 
    texto_novo += texto[t]

print(texto_novo)