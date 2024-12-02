####################################################
## 3. Fluxo de Controle e Iteráveis
####################################################

# Vamos apenas criar uma variável
some_var = 5

# Aqui está uma instrução if. A indentação é significativa em Python!
# A convenção é usar quatro espaços, não tabs.
# Isso imprime "some_var é menor que 10"
if some_var > 10:
    print("some_var é totalmente maior que 10.")
elif some_var < 10:    # Esta cláusula elif é opcional.
    print("some_var é menor que 10.")
else:                  # Isso também é opcional.
    print("some_var é de fato 10.")


"""
Os loops for iteram sobre listas
imprime:
    cachorro é um mamífero
    gato é um mamífero
    rato é um mamífero
"""
for animal in ["dog", "cat", "mouse"]:
    # Você pode usar format() para interpolar strings formatadas
    print("{} é um mamífero".format(animal))

"""
"range(número)" retorna um iterável de números
de zero até (mas excluindo) o número dado
imprime:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
"range(inferior, superior)" retorna um iterável de números
do número inferior até o número superior
imprime:
    4
    5
    6
    7
"""
for i in range(4, 8):
    print(i)

"""
"range(inferior, superior, passo)" retorna um iterável de números
do número inferior até o número superior, incrementando
pelo passo. Se o passo não for indicado, o valor padrão é 1.
imprime:
    4
    6
"""
for i in range(4, 8, 2):
    print(i)

"""
Percorre uma lista para recuperar tanto o índice quanto o valor de cada item da lista:
    0 cachorro
    1 gato
    2 rato
"""
animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print(i, value)

"""
Os loops while vão até que uma condição não seja mais atendida.
imprime:
    0
    1
    2
    3
"""

x = 0
while x < 4:
    print(x)
    x += 1  # Atalho para x = x + 1

# Trata exceções com um bloco try/except
try:
    # Use "raise" para levantar um erro
    raise IndexError("Este é um erro de índice")
except IndexError as e:
    pass                 # Evite isso, forneça uma recuperação (próximo exemplo).
except (TypeError, NameError):
    pass                 # Múltiplas exceções podem ser processadas juntas.
else:                    # Cláusula opcional ao bloco try/except. Deve seguir
                         # todos os blocos except.
    print("Tudo certo!") # Executa somente se o código em try não levantar exceções
finally:                 # Executa sob todas as circunstâncias
    print("Podemos limpar os recursos aqui")

# Em vez de try/finally para limpar recursos, você pode usar uma declaração with
with open("myfile.txt") as f:
    for line in f:
        print(line)

# Escrevendo em um arquivo
contents = {"aa": 12, "bb": 21}
with open("myfile1.txt", "w") as file:
    file.write(str(contents))        # escreve uma string em um arquivo

import json
with open("myfile2.txt", "w") as file:
    file.write(json.dumps(contents))  # escreve um objeto em um arquivo

# Lendo de um arquivo
with open("myfile1.txt") as file:
    contents = file.read()           # lê uma string de um arquivo
print(contents)
# print: {"aa": 12, "bb": 21}

with open("myfile2.txt", "r") as file:
    contents = json.load(file)       # lê um objeto json de um arquivo
print(contents)
# print: {"aa": 12, "bb": 21}


# Python oferece uma abstração fundamental chamada Iterable.
# Um iterable é um objeto que pode ser tratado como uma sequência.
# O objeto retornado pela função range é um iterable.

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable)  # => dict_keys(['one', 'two', 'three']). Este é um objeto
                     # que implementa nossa interface Iterable.

# Podemos percorrer isso.
for i in our_iterable:
    print(i)  # Imprime one, two, three

# No entanto, não podemos acessar elementos por índice.
our_iterable[1]  # Levanta um TypeError

# Um iterable é um objeto que sabe como criar um iterator.
our_iterator = iter(our_iterable)

# Nosso iterator é um objeto que pode lembrar o estado enquanto percorremos
# ele. Obtemos o próximo objeto com "next()".
next(our_iterator)  # => "one"

# Ele mantém o estado enquanto iteramos.
next(our_iterator)  # => "two"
next(our_iterator)  # => "three"

# Depois que o iterator retornou todos os seus dados, ele levanta uma
# exceção StopIteration
next(our_iterator)  # Levanta StopIteration

# Também podemos percorrê-lo, na verdade, "for" faz isso implicitamente!
our_iterator = iter(our_iterable)
for i in our_iterator:
    print(i)  # Imprime one, two, three

# Você pode pegar todos os elementos de um iterable ou iterator chamando list().
list(our_iterable)  # => Retorna ["one", "two", "three"]
list(our_iterator)  # => Retorna [] porque o estado é salvo

