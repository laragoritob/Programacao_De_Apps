def potencia():
    c = 1
 # QUALQUER NÚMERO ELEVADO A 0 É 1 #
    if (b == 0):
        return 1
 # MULTIPLICA 'a' POR ELE MESMO 'b' VEZES #
    for i in range (b):
        c = c * a
 # SE O EXPOENTE FOR NEGATIVO, INVERTERÁ O RESULTADO #
    if (b < 0):
        c = 1 / c
    return c

a = int(input("Digite o número base: "))
b = int(input("Digite o número da potência: "))
c = potencia()

print(f"{a}^{b} = {c}")


