def pre_process(texto):
    texto = texto.lower()
    tabela = str.maketrans("", "", "!,.😍")
    texto = texto.translate(tabela)
    return texto

texto = "Adorei o produto! Super recomendo 😍"
print(pre_process(texto)) 