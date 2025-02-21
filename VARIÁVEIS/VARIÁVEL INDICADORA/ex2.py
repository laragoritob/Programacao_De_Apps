n = int(input("Digite uma quantidade de números para ser analisada: "))
print("Informe o número: ")
anterior = int(input())

i = 1 # LEU UM NÚMERO
ordenado = True # ORDENADO É A VARIÁVEL INDICADORA

while (i < n) and (ordenado):
    print("Informe o número: ")
    atual = int(input())
    i = i + 1 # LEU MAIS UM NÚMERO
    
    if (atual < anterior):
        ordenado = False
    anterior = atual

if (ordenado):
    print("Sequência ordenada.")
else:
    print("Sequência não ordenada.")
