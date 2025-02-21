def PosOuNeg(numero):
    if numero < 0:
        return 'N'
    elif numero > 0:
        return 'P'
    else:
        return 'Z'
    
numero = int(input("Digite um número: "))
resultado = PosOuNeg(numero)
print(f"O resultado é: {resultado}")