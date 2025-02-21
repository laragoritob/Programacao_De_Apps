def reverso():
    reverso = " "
    for x in n:
        reverso = x + reverso
    return reverso

n = (input("Digite um número: "))
print(f"O inverso desse número é: {reverso()}")