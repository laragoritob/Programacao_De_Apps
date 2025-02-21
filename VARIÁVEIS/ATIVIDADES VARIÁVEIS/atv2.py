import random  # Importa o módulo random para gerar números aleatórios, usado para a escolha do computador

# Função que simula uma rodada do jogo Pedra, Papel e Tesoura
def jogar():
    opcoes = ["Pedra", "Papel", "Tesoura"]  # Lista contendo as opções possíveis para o jogo
    
    # Solicita a escolha do jogador, que pode digitar 0, 1 ou 2
    jogador = input("Escolha: 0 (Pedra), 1 (Papel), 2 (Tesoura): ")
    
    # Verifica se a entrada do jogador é válida (0, 1 ou 2)
    if jogador not in ["0", "1", "2"]:
        print("Opção inválida")  # Se a entrada for inválida, imprime mensagem e encerra a função
        return False  # Retorna False para não continuar o jogo
    
    jogador = int(jogador)  # Converte a entrada do jogador para um número inteiro (0, 1 ou 2)
    
    # O computador escolhe aleatoriamente entre 0 (Pedra), 1 (Papel) e 2 (Tesoura)
    computador = random.randint(0, 2)  # Gera um número aleatório entre 0 e 2
    
    # Exibe as escolhas do jogador e do computador
    print(f"\nVocê escolheu: {opcoes[jogador]}")  
    print(f"O computador escolheu: {opcoes[computador]}")
    
    # Determina o vencedor
    if jogador == computador:
        print("Empate!")  # Se ambos escolherem a mesma opção, é um empate
    # Verifica quem venceu, de acordo com as regras do jogo
    elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
        print("Você venceu!")  # O jogador vence se a escolha dele for superior à do computador
    else:
        print("Você perdeu!")  # Caso contrário, o jogador perde
    
    return True  # Retorna True para indicar que o jogo pode continuar

# Função principal que gerencia o fluxo do jogo
def main():
    while True:  # O loop continuará enquanto o jogador desejar jogar
        # Chama a função 'jogar' para uma nova rodada
        if not jogar():
            break  # Se a opção do jogador for inválida, o loop é interrompido
        
        # Pergunta ao jogador se ele deseja jogar novamente
        jogar_novamente = input("\nQuer jogar novamente? (Sim/Não): ").strip().lower()  # Recebe a resposta e remove espaços extras
        
        # Se o jogador não responder com 'sim', o jogo é encerrado
        if jogar_novamente != "sim":
            print("Obrigado por jogar! Até a próxima.")  # Mensagem de despedida
            break  # Encerra o loop e o programa

# Chama a função principal para iniciar o jogo
main()
