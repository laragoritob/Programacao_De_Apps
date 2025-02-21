qnt = int(input("Digite a quantidade de notas: "))
notas = []

for i in range(qnt):
    nota = float(input(f"Digite a {i + 1}ª nota: ")) # LÊ A 'i' NOTA COMO UM NÚMERO DE PONTO FLUTUANTE (FLOAT) #
    notas.append(nota) # ADICIONA A NOTA À LISTA DE NOTAS #

print("As notas digitadas foram:" ,notas)

media = sum(notas) / qnt # CÁLCULO MÉDIA #
print("A média das notas é: ", media) 