# MOSTRAR AS 'n' NOTAS #
notas = []
n = int(input("Digite o número de notas: "))

for i in range(n):
    dado = float(input(f"Digite a nota {i + 1}: "))
    notas.append(dado)

print(notas)

# CALCULAR A MÉDIA #
soma = 0

for i in range(len(notas)):
    soma = soma + notas[i]

media = soma / len(notas)

print(format(media, ".1f"))