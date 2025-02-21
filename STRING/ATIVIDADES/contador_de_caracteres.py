texto = input("Digite um texto: ")
pontuacao = [".", ",", ":", ";", "!", "?"]

# REMOVE OS SINAIS DE PONTUAÇÃO
for p in pontuacao:
    texto = texto.replace(p," ")

# SPLIT DEVOLVE LISTA COM PALAVRAS COMO ITENS
numero_palavras = len(texto)
print("Número de palavras:", numero_palavras) 