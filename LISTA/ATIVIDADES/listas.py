# LÊ AS DUAS LISTAS COM 5 INTEIROS CADA
lista1 = []
lista2 = []

print("--------- VALORES DA PRIMEIRA LISTA ------------")
for i in range(5):
    # LÊ O VALOR E ADICIONA NA PRIMEIRA LISTA
    lista1.append(int(input(f"Digite o {i + 1}º valor: ")))

print("\n--------- VALORES DA SEGUNDA LISTA ------------")
for i in range(5):
    # LÊ O VALOR E ADICIONA NA SEGUNDA LISTA
    lista2.append(int(input(f"Digite o {i + 1}º valor: ")))

# CHECA QUAIS ELEMENTOS DA SEGUNDA LISTA ESTÃO NA PRIMEIRA LISTA
comum = []

# LOOP PARA VERIFICAR ELEMENTOS COMUNS ENTRE AS LISTAS
for numero in lista2:
    # SE O NÚMERO ESTIVER NA PRIMEIRA LISTA, ADICIONA À LISTA DE COMUNS
    if numero in lista1:
        comum.append(numero)

# SE HOUVER ELEMENTOS COMUNS, EXIBE-OS; CASO CONTRÁRIO, INFORMA QUE NÃO HÁ
if comum:
    # EXIBE OS ELEMENTOS EM COMUM
    for elemento in comum:
        print("O(s) número(s) em comum:", elemento)
else:
    # INFORMA QUE NÃO TEM ELEMENTOS EM COMUM
    print("Não tem.")
