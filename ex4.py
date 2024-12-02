def normalize(texto): 
    texto = texto.lower()
    dicionario_substituicoes = {
        "vc": "você",
        "eh": "é",
        "mto": "muito",
        "mt": "muito", 
        "bom": "bom",  # Mantém como está, mas pode ser útil para referências
        "recomendo": "recomendo",  # Mantém como está
        "!!!": "",  # Remove múltiplos sinais de exclamação
        "!": "",  # Remove sinais de exclamação isolados
        "eae": "e aí",
        "blz": "beleza",
        "tb": "também",
        "pq": "porque",
        "q": "que",
        "vc": "você",
        "td": "tudo"
    }
    for chave, valor in dicionario_substituicoes.items():
        texto = texto.replace(chave, valor)
    return texto