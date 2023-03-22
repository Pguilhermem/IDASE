class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("Olá!")
    

class Estudante(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)
        self.curso = curso

    def falar(self):
        print(f"Olá, meu nome é {self.nome} e eu faço {self.curso}.")
    
class Trabalhador(Pessoa):
    def __init__(self, nome, empresa):
        super().__init__(nome)
        self.empresa = empresa

    def falar(self):
        print(f"Olá, meu nome é {self.nome} e eu trabalho na empresa {self.empresa}.")