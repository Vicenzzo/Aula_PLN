####################################################
## 2. Variáveis e Coleções
####################################################

# Python tem uma função print
print("I'm Python. Nice to meet you!")  # => I'm Python. Nice to meet you!

# Por padrão, a função print também imprime uma nova linha no final.
# Use o argumento opcional end para mudar a string final.
print("Hello, World", end="!")  # => Hello, World!

# Maneira simples de obter dados de entrada do console
input_string_var = input("Enter some data: ")  # Retorna os dados como uma string

# Não há declarações, apenas atribuições.
# A convenção para nomear variáveis é o estilo snake_case
some_var = 5
some_var  # => 5

# Acessar uma variável previamente não atribuída gera uma exceção.
# Veja Controle de Fluxo para aprender mais sobre tratamento de exceções.
some_unknown_var  # Levanta um NameError

# if pode ser usado como uma expressão
# Equivalente ao operador ternário '?:' em C
"yay!" if 0 > 1 else "nay!"  # => "nay!"

# Listas armazenam sequências
li = []
# Você pode começar com uma lista pré-preenchida
other_li = [4, 5, 6]

# Adicione itens ao final de uma lista com append
li.append(1)    # li agora é [1]
li.append(2)    # li agora é [1, 2]
li.append(4)    # li agora é [1, 2, 4]
li.append(3)    # li agora é [1, 2, 4, 3]
# Remova do final com pop
li.pop()        # => 3 e li agora é [1, 2, 4]
# Vamos colocá-lo de volta
li.append(3)    # li agora é [1, 2, 4, 3] novamente.

# Acesse uma lista como você faria com qualquer array
li[0]   # => 1
# Veja o último elemento
li[-1]  # => 3

# Olhar fora dos limites gera um IndexError
li[4]  # Levanta um IndexError

# Você pode olhar para intervalos com a sintaxe de fatiamento.
# O índice de início é incluído, o índice final não.
# (É um intervalo fechado/aberto para você que é matemático.)
li[1:3]   # Retorna a lista do índice 1 ao 3 => [2, 4]
li[2:]    # Retorna a lista começando do índice 2 => [4, 3]
li[:3]    # Retorna a lista do início até o índice 3  => [1, 2, 4]
li[::2]   # Retorna a lista selecionando elementos com um tamanho de passo de 2 => [1, 4]
li[::-1]  # Retorna a lista na ordem inversa => [3, 4, 2, 1]
# Use qualquer combinação dessas para fazer fatiamentos avançados
# li[start:end:step]

# Faça uma cópia rasa usando fatiamento
li2 = li[:]  # => li2 = [1, 2, 4, 3], mas (li2 é li) resultará em falso.


# Remove elementos arbitrários de uma lista com "del"
del li[2]  # li agora é [1, 2, 3]

# Remove a primeira ocorrência de um valor
li.remove(2)  # li agora é [1, 3]
li.remove(2)  # Levanta um ValueError pois 2 não está na lista

# Insere um elemento em um índice específico
li.insert(1, 2)  # li agora é [1, 2, 3] novamente

# Obtém o índice do primeiro item encontrado que corresponde ao argumento
li.index(2)  # => 1
li.index(4)  # Levanta um ValueError pois 4 não está na lista

# Você pode adicionar listas
# Nota: os valores de li e de other_li não são modificados.
li + other_li  # => [1, 2, 3, 4, 5, 6]

# Concatena listas com "extend()"
li.extend(other_li)  # Agora li é [1, 2, 3, 4, 5, 6]

# Verifica a existência em uma lista com "in"
1 in li  # => True

# Examina o comprimento com "len()"
len(li)  # => 6


# Tuplas são como listas, mas são imutáveis.
tup = (1, 2, 3)
tup[0]      # => 1
tup[0] = 3  # Levanta um TypeError

# Nota que uma tupla de comprimento um precisa ter uma vírgula após o último elemento, mas
# tuplas de outros comprimentos, até mesmo zero, não.
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>

# Você pode fazer a maioria das operações de lista em tuplas também
len(tup)         # => 3
tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
tup[:2]          # => (1, 2)
2 in tup         # => True

# Você pode desempacotar tuplas (ou listas) em variáveis
a, b, c = (1, 2, 3)  # a agora é 1, b agora é 2 e c agora é 3
# Você também pode fazer desempacotamento estendido
a, *b, c = (1, 2, 3, 4)  # a agora é 1, b agora é [2, 3] e c agora é 4
# Tuplas são criadas por padrão se você deixar de fora os parênteses
d, e, f = 4, 5, 6  # a tupla 4, 5, 6 é desempacotada nas variáveis d, e e f
# respectivamente, onde d = 4, e = 5 e f = 6
# Agora veja como é fácil trocar dois valores
e, d = d, e  # d agora é 5 e e agora é 4


# Dicionários armazenam mapeamentos de chaves para valores
empty_dict = {}
# Aqui está um dicionário pré-preenchido
filled_dict = {"one": 1, "two": 2, "three": 3}

# Nota: as chaves para dicionários precisam ser tipos imutáveis. Isso é para garantir que
# a chave possa ser convertida em um valor hash constante para buscas rápidas.
# Tipos imutáveis incluem ints, floats, strings, tuplas.
invalid_dict = {[1,2,3]: "123"}  # => Levanta um TypeError: tipo não hashable: 'list'
valid_dict = {(1,2,3):[1,2,3]}   # Os valores podem ser de qualquer tipo, no entanto.

# Procura valores com []
filled_dict["one"]  # => 1

# Obtém todas as chaves como um iterável com "keys()". Precisamos envolver a chamada em list()
# para transformá-la em uma lista. Vamos falar sobre isso mais tarde. Nota - para versões do Python
# <3.7, a ordenação das chaves do dicionário não é garantida. Seus resultados podem
# não corresponder exatamente ao exemplo abaixo. No entanto, a partir do Python 3.7, os itens do dicionário
# mantêm a ordem em que foram inseridos no dicionário.
list(filled_dict.keys())  # => ["three", "two", "one"] em Python <3.7
list(filled_dict.keys())  # => ["one", "two", "three"] em Python 3.7+


# Obtém todos os valores como um iterável com "values()". Novamente, precisamos envolvê-lo
# em list() para tirá-lo do iterável. Nota - O mesmo se aplica à ordenação das chaves.
list(filled_dict.values())  # => [3, 2, 1]  em Python <3.7
list(filled_dict.values())  # => [1, 2, 3] em Python 3.7+

# Verifica a existência de chaves em um dicionário com "in"
"one" in filled_dict  # => True
1 in filled_dict      # => False

# Procurar uma chave não existente gera um KeyError
filled_dict["four"]  # KeyError

# Use o método "get()" para evitar o KeyError
filled_dict.get("one")      # => 1
filled_dict.get("four")     # => None
# O método get suporta um argumento padrão quando o valor está ausente
filled_dict.get("one", 4)   # => 1
filled_dict.get("four", 4)  # => 4

# "setdefault()" insere em um dicionário apenas se a chave dada não estiver presente
filled_dict.setdefault("five", 5)  # filled_dict["five"] é definido como 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] ainda é 5

# Adicionando a um dicionário
filled_dict.update({"four":4})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4         # outra maneira de adicionar ao dict

# Remove chaves de um dicionário com del
del filled_dict["one"]  # Remove a chave "one" do dicionário preenchido

# A partir do Python 3.5, você também pode usar as opções de desempacotamento adicionais
{"a": 1, **{"b": 2}}  # => {'a': 1, 'b': 2}
{"a": 1, **{"a": 2}}  # => {'a': 2}


# Conjuntos armazenam... bem, conjuntos
empty_set = set()
# Inicializa um conjunto com alguns valores.
some_set = {1, 1, 2, 2, 3, 4}  # some_set agora é {1, 2, 3, 4}

# Semelhante às chaves de um dicionário, os elementos de um conjunto devem ser imutáveis.
invalid_set = {[1], 1}  # => Levanta um TypeError: tipo não hashable: 'list'
valid_set = {(1,), 1}

# Adiciona mais um item ao conjunto
filled_set = some_set
filled_set.add(5)  # filled_set agora é {1, 2, 3, 4, 5}
# Conjuntos não têm elementos duplicados
filled_set.add(5)  # permanece como antes {1, 2, 3, 4, 5}

# Faz interseção de conjuntos com &
other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}

# Faz união de conjuntos com |
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}

# Faz diferença de conjuntos com -
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}

# Faz diferença simétrica de conjuntos com ^
{1, 2, 3, 4} ^ {2, 3, 5}  # => {1, 4, 5}

# Verifica se o conjunto à esquerda é um superconjunto do conjunto à direita
{1, 2} >= {1, 2, 3}  # => False

# Verifica se o conjunto à esquerda é um subconjunto do conjunto à direita
{1, 2} <= {1, 2, 3}  # => True

# Verifica a existência em um conjunto com in
2 in filled_set   # => True
10 in filled_set  # => False

# Faz uma cópia de um nível
filled_set = some_set.copy()  # filled_set é {1, 2, 3, 4, 5}
filled_set is some_set        # => False


