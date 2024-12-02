comentarios = [
    {"autor": "João", "comentario": "Estou tão feliz hoje!", "sentimento": "Positivo"},
    {"autor": "Maria", "comentario": "Este filme é tão triste.", "sentimento": "Negativo"},
    {"autor": "Carlos", "comentario": "Que dia chuvoso entediante...", "sentimento": "Negativo"},
    {"autor": "Ana", "comentario": "Adorei a nova música da banda!", "sentimento": "Positivo"},
    {"autor": "Roberto", "comentario": "Eureka, consegui resolver este problema", "sentimento": "Positivo"}
]


for comentario in comentarios:
    comentario["sentimento_valor"] = 1 if comentario["sentimento"] == "Positivo" else 0

positivos = sum(comentario["sentimento_valor"] for comentario in comentarios)
negativos = len(comentarios) - positivos

total_comentarios = len(comentarios)
proporcao_positivos = (positivos / total_comentarios) * 100
proporcao_negativos = (negativos / total_comentarios) * 100

print(f"Proporção de comentários positivos: {proporcao_positivos:.2f}%")
print(f"Proporção de comentários negativos: {proporcao_negativos:.2f}%")

comentarios_positivos = [comentario for comentario in comentarios if comentario["sentimento_valor"] == 1]

print("\nComentários Positivos:")
for comentario in comentarios_positivos:
    print(f"{comentario['autor']}: {comentario['comentario']}")
