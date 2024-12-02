# Os comentários de linha única começam com um símbolo de número.

""" Strings multilinha podem ser escritas
    usando três "s, e são frequentemente usadas
    como documentação.
"""

####################################################
## 1. Tipos de Dados Primitivos e Operadores
####################################################

# Você tem números
3  # => 3

# A matemática é o que você esperaria
1 + 1   # => 2
8 - 1   # => 7
10 * 2  # => 20
35 / 5  # => 7.0

# A divisão inteira arredonda para o infinito negativo
5 // 3       # => 1
-5 // 3      # => -2
5.0 // 3.0   # => 1.0  # funciona com floats também
-5.0 // 3.0  # => -2.0


# O resultado da divisão é sempre um float
10.0 / 3  # => 3.3333333333333335

# Operação de módulo
7 % 3   # => 1
# i % j têm o mesmo sinal que j, ao contrário de C
-7 % 3  # => 2

# Exponenciação (x**y, x elevado à potência y)
2**3  # => 8

# Imponha precedência com parênteses
1 + 3 * 2    # => 7
(1 + 3) * 2  # => 8

# Valores booleanos são primitivos (Nota: a capitalização)
True   # => True
False  # => False

# Negar com not
not True   # => False
not False  # => True

# Operadores Booleanos
# Nota: "and" e "or" são sensíveis a maiúsculas
True and False  # => False
False or True   # => True

# True e False são na verdade 1 e 0, mas com palavras-chave diferentes
True + True  # => 2
True * 8     # => 8
False - 5    # => -5

# Operadores de comparação olham para o valor numérico de True e False
0 == False   # => True
2 > True     # => True
2 == True    # => False
-5 != False  # => True

# None, 0 e strings/listas/dicionários/tuplas/conjuntos vazios avaliam como False.
# Todos os outros valores são True
bool(0)      # => False
bool("")     # => False
bool([])     # => False
bool({})     # => False
bool(())     # => False
bool(set())  # => False
bool(4)      # => True
bool(-6)     # => True

# Usando operadores lógicos booleanos em ints os converte em booleanos para avaliação,
# mas seu valor não convertido é retornado. Não confunda com bool(ints) e bitwise
# and/or (&,|).
bool(0)   # => False
bool(2)   # => True
0 and 2   # => 0
bool(-5)  # => True
bool(2)   # => True
-5 or 0   # => -5

# Igualdade é ==
1 == 1  # => True
2 == 1  # => False

# Desigualdade é !=
1 != 1  # => False
2 != 1  # => True

# Mais comparações
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Verificando se um valor está em um intervalo
1 < 2 and 2 < 3  # => True
2 < 3 and 3 < 2  # => False
# A cadeia torna isso mais elegante
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# (is vs. ==) is verifica se duas variáveis se referem ao mesmo objeto, mas == verifica
# se os objetos apontados têm os mesmos valores.
a = [1, 2, 3, 4]  # Aponta a para uma nova lista, [1, 2, 3, 4]
b = a             # Aponta b para o que a está apontando
b is a            # => True, a e b se referem ao mesmo objeto
b == a            # => True, os objetos de a e b são iguais
b = [1, 2, 3, 4]  # Aponta b para uma nova lista, [1, 2, 3, 4]
b is a            # => False, a e b não se referem ao mesmo objeto
b == a            # => True, os objetos de a e b são iguais

# Strings são criadas com " ou '
"This is a string."
'This is also a string.'

# Strings também podem ser somadas
"Hello " + "world!"  # => "Hello world!"
# Literais de string (mas não variáveis) podem ser concatenados sem usar '+'
"Hello " "world!"    # => "Hello world!"

# Uma string pode ser tratada como uma lista de caracteres
"Hello world!"[0]  # => 'H'

# Você pode encontrar o comprimento de uma string
len("This is a string")  # => 16

# Desde o Python 3.6, você pode usar f-strings ou literais de string formatados.
name = "Reiko"
f"She said her name is {name}."  # => "She said her name is Reiko"
# Qualquer expressão Python válida dentro dessas chaves é retornada para a string.
f"{name} is {len(name)} characters long."  # => "Reiko is 5 characters long."

# None é um objeto
None  # => None

# Não use o símbolo de igualdade "==" para comparar objetos com None
# Use "is" em vez disso. Isso verifica a igualdade da identidade do objeto.
"etc" is None  # => False
None is None   # => True