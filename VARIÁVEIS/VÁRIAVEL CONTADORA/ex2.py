n = int(input("Digite uma quantidade de números para ser analisada: "))
print("Informe o número: ")
anterior = int(input())

i = 1 # LEU UM NÚMERO
ordenado = 0 # ORDENADO É A VARIÁVEL CONTADORA

while (i < n) and (ordenado == 0):
    print("Informe o número: ")
    atual = int(input())
    i = i + 1 # LEU MAIS UM NÚMERO
    
    if (atual <= anterior):
        ordenado = ordenado + 1
    anterior = atual

if (ordenado == 0):
    print("Sequência ordenada.")
else:
    print("Sequência não ordenada.")
