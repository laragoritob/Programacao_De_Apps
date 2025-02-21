# Função para verificar se um número tem dígitos adjacentes iguais
def num_iguais(num):
    num_str = str(num)  # Converte o número em uma string para verificar cada dígito

    # Percorre a string de números, verificando se dois dígitos adjacentes são iguais
    for i in range(len(num_str) - 1):  # Acessa cada posição do número até o penúltimo dígito
        if num_str[i] == num_str[i + 1]:  # Compara o dígito atual com o próximo
            return True  # Se encontrar dígitos adjacentes iguais, retorna True
    return False  # Caso não encontre dígitos adjacentes iguais, retorna False

i = 1  # Inicializa a variável i para controlar o número de repetições

# Enquanto i for menor ou igual a 5, o loop continuará
while (i <= 5):  
    n = int(input("Digite um número inteiro: "))  # Solicita que o usuário digite um número inteiro

    # Chama a função num_iguais para verificar se o número tem dígitos adjacentes iguais
    if num_iguais(n):
        print("É adjacente.")  # Informa que o número tem dígitos adjacentes iguais
    else:
        print("Não é adjacente.")  # Informa que o número não tem dígitos adjacentes iguais

    i = i + 1  # Incrementa a variável i para garantir que o loop seja repetido 5 vezes
