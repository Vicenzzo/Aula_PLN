####################################################
## 4. Funções
####################################################

# Use "def" para criar novas funções
def add(x, y):
    print("x é {} e y é {}".format(x, y))
    return x + y  # Retorna valores com uma declaração return

# Chamando funções com parâmetros
add(5, 6)  # => imprime "x é 5 e y é 6" e retorna 11

# Outra maneira de chamar funções é com argumentos nomeados
add(y=6, x=5)  # Argumentos nomeados podem chegar em qualquer ordem.

# Você pode definir funções que aceitam um número variável de
# argumentos posicionais
def varargs(*args):
    return args

varargs(1, 2, 3)  # => (1, 2, 3)

# Você também pode definir funções que aceitam um número variável de
# argumentos nomeados
def keyword_args(**kwargs):
    return kwargs

# Vamos chamá-la para ver o que acontece
keyword_args(big="foot", loch="ness")  # => {"big": "foot", "loch": "ness"}


# Você pode fazer os dois ao mesmo tempo, se quiser
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
"""
all_the_args(1, 2, a=3, b=4) imprime:
    (1, 2)
    {"a": 3, "b": 4}
"""

# Ao chamar funções, você pode fazer o oposto de args/kwargs!
# Use * para expandir args (tuplas) e use ** para expandir kwargs (dicionários).
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)            # equivalente: all_the_args(1, 2, 3, 4)
all_the_args(**kwargs)         # equivalente: all_the_args(a=3, b=4)
all_the_args(*args, **kwargs)  # equivalente: all_the_args(1, 2, 3, 4, a=3, b=4)

# Retornando múltiplos valores (com atribuições de tupla)
def swap(x, y):
    return y, x  # Retorna múltiplos valores como uma tupla sem os parênteses.
                 # (Nota: os parênteses foram excluídos, mas podem ser incluídos)

x = 1
y = 2
x, y = swap(x, y)     # => x = 2, y = 1
# (x, y) = swap(x,y)  # Novamente, o uso de parênteses é opcional.

# escopo global
x = 5

def set_x(num):
    # o escopo local começa aqui
    # a variável local x não é a mesma que a variável global x
    x = num    # => 43
    print(x)   # => 43

def set_global_x(num):
    # global indica que a variável em particular vive no escopo global
    global x
    print(x)   # => 5
    x = num    # a variável global x agora é definida como 6
    print(x)   # => 6

set_x(43)
set_global_x(6)
"""
imprime:
    43
    5
    6
"""

# Python tem funções de primeira classe
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)   # => 13

# Fechamentos em funções aninhadas:
# Podemos usar a palavra-chave nonlocal para trabalhar com variáveis em escopos aninhados que não devem ser declaradas nas funções internas.
def create_avg():
    total = 0
    count = 0
    def avg(n):
        nonlocal total, count
        total += n
        count += 1
        return total/count
    return avg
avg = create_avg()
avg(3)  # => 3.0
avg(5)  # (3+5)/2 => 4.0
avg(7)  # (8+7)/3 => 5.0

# Também existem funções anônimas
(lambda x: x > 2)(3)                  # => True
(lambda x, y: x ** 2 + y ** 2)(2, 1)  # => 5

# Existem funções de ordem superior embutidas
list(map(add_10, [1, 2, 3]))          # => [11, 12, 13]
list(map(max, [1, 2, 3], [4, 2, 1]))  # => [4, 2, 3]

list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))  # => [6, 7]

# Podemos usar compreensões de lista para mapas e filtros agradáveis
# A compreensão de lista armazena a saída como uma lista (que pode ser aninhada).
[add_10(i) for i in [1, 2, 3]]         # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

# Você também pode construir compreensões de conjunto e dicionário.
{x for x in "abcddeef" if x not in "abc"}  # => {'d', 'e', 'f'}
{x: x**2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}