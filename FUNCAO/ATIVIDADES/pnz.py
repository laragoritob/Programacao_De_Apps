# FUNÇÃO COM AS CONDIÇÕES #
def pnz():
    if(n > 0):
        print("O resultado é: P!")
    elif(n < 0):
        print("O resultado é: N!")
    else:
        print("O resultado é: Z!")
    
n = int(input("Digite um número: "))

# CHAMA A FUNÇÃO PARA VERIFICAR E IMPRIMIR #
pnz()
