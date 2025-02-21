class Conta:
    numero = "00000-0"
    saldo = 0.0

    def deposito(self, valor):
        self.saldo += valor # CONTA PARA ADICIONAR VALOR #

    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor # CONTA PARA RETIRAR VALOR #
        else:
            print("Saldo insuficiente.")


    print(saldo)
    print(numero)