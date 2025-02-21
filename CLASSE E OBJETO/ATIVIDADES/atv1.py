class Pessoa:
    nome = ""
    idade = 0
    peso = 0
    altura = 0

    def envelhecer(self, ano): 
        self.idade += ano

    def engordar(self, kg):  
        self.peso += kg

    def emagrecer(self, kg):
        self.peso -= kg

    def crescer(self, ano):
        if (self.idade < 21):
            self.altura += (0.05 * ano)

if __name__ == '__main__':
    pessoa = Pessoa()
    pessoa.nome = "Guilherme"
    pessoa.idade = 17
    pessoa.peso = 55
    pessoa.altura = 1.66


    print("Nome:", pessoa.nome, "/" ,"Idade:", pessoa.idade, "/", "Peso:", pessoa.peso, "/", "Altura:", pessoa.altura)
    pessoa.envelhecer(3)
    pessoa.engordar(10)
    pessoa.crescer(3)
    print("Nome:", pessoa.nome, "/" ,"Idade:", pessoa.idade, "/", "Peso:", pessoa.peso, "/", "Altura:", pessoa.altura)
    pessoa.emagrecer(5)
    print("Nome:", pessoa.nome, "/" ,"Idade:", pessoa.idade, "/", "Peso:", pessoa.peso, "/", "Altura:", pessoa.altura)