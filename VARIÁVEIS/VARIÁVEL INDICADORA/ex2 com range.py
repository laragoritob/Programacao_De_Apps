n = int(input("Digite uma quantidade de números para ser analisada: "))
print("Informe o número: ")
anterior = int(input())

i = 1 # LEU UM NÚMERO
ordenado = True # ORDENADO É A VARIÁVEL INDICADORA

for i in range(n-1):
    print("Informe o número: ")
    atual = int(input())
    
    if (atual < anterior):
        ordenado = False
        break
    anterior = atual

if (ordenado):
    print("Sequência ordenada.")
else:
    print("Sequência não ordenada.")
