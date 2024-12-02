####################################################
## 5. Módulos
####################################################

# Você pode importar módulos
import math
print(math.sqrt(16))  # => 4.0

# Você pode obter funções específicas de um módulo
from math import ceil, floor
print(ceil(3.7))   # => 4
print(floor(3.7))  # => 3

# Você pode importar todas as funções de um módulo.
# Aviso: isso não é recomendado
from math import *

# Você pode encurtar nomes de módulos
import math as m
math.sqrt(16) == m.sqrt(16)  # => True

# Módulos Python são apenas arquivos Python comuns.
# Você pode escrever o seu próprio e importá-los. O nome do
# módulo é o mesmo que o nome do arquivo.

# Você pode descobrir quais funções e atributos
# estão definidos em um módulo.
import math
dir(math)

# Se você tiver um script Python chamado math.py na mesma
# pasta que seu script atual, o arquivo math.py será
# carregado em vez do módulo embutido do Python.
# Isso acontece porque a pasta local tem prioridade
# sobre as bibliotecas embutidas do Python.