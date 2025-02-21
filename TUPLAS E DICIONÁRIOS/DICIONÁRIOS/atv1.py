# Solicita ao usuário que digite uma palavra ou frase
string = input("Digite uma palavra: ")

# Dicionário para contar as ocorrências das letras
contagem = {}

# Lista de pontuações que serão removidas da string
pontuacao = [".", ",", ":", ";", "!", "?"]

# REMOVE OS SINAIS DE PONTUAÇÃO
for p in pontuacao:  # Para cada sinal de pontuação na lista
    string = string.replace(p," ")  # Substitui o sinal de pontuação por um espaço em branco

# Contagem das letras na string (agora sem pontuação)
for letra in string:
    if letra in contagem:  # Se a letra já foi encontrada, incrementa a contagem
        contagem[letra] = contagem[letra] + 1
    else:  # Se a letra não foi encontrada antes, adiciona ela ao dicionário com valor 1
        contagem[letra] = 1

# Variável para armazenar a letra com a maior contagem
mais = ''

# Procura a letra com o maior número de ocorrências
for key in contagem:
    if not mais or contagem[key] > contagem[mais]:  # Se for a primeira letra ou a contagem for maior que a atual
        mais = key  # Atualiza a letra mais comum

# Exibe a letra que mais se repete
print("A letra que mais repete é:", mais)
