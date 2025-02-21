# Solicita ao usuário que digite um texto
string = input("Digite um texto: ")
# Inicializa uma string vazia para armazenar a inversa do texto
inversa = ""

# Converte toda a string para minúsculas para evitar problemas com maiúsculas e minúsculas
stringlower = string.lower()

# Define uma lista de pontuações que queremos remover da string
pontuacao = [".", ",", ":", ";", "!", "?"]

# Remove as pontuações da string
for p in pontuacao:
    stringlower = stringlower.replace(p, "")

# Cria a inversa da string sem pontuação e em minúsculas
for x in stringlower:
    inversa = x + inversa  # Aqui a cada letra é adicionada na frente da string inversa, invertendo a ordem

# Exibe a string invertida
print(inversa)

# Compara a string sem pontuação e em minúsculas com a sua inversa
if stringlower == inversa:
    print("É palíndromo.")  # Se forem iguais, o texto é um palíndromo
else:
    print("Não é palíndromo.")  # Se forem diferentes, o texto não é um palíndromo
