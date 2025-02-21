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


if __name__ == '__main__':
    conta = Conta()
    conta.saldo = 20
    conta.numero = "13131-2"
    conta.deposito(10) # VALOR PARA ADICIONAR NO SALDO #
    conta.saque(50)
    print(conta.saldo)
    print(conta.numero)