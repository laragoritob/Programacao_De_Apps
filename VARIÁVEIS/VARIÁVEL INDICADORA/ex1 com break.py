n = int(input("Digite um número inteiro positivo: "))

numero = 2
primo = True # PRIMO É A VARIÁVEL INDICADORA #

while (numero <= n-1):
    if (n % numero == 0): # SE 'n' É DIVISÍVEL POR NÚMERO
        primo = False
        break
    numero = numero + 1

if (primo):
    print("É primo.")
else:
    print("Não é primo.")