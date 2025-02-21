def f1(a):
    print(a+x)

def f3(a):
    x = x + 1
    print(a+x)

x = 4

f1(3)
f3(3) # ESTE COMANDO VAI DAR ERRO, POIS ESTÁ SENDO UTILIZADO UMA VARIÁVEL LOCAL 'x' ANTES DE SER CRIADA #