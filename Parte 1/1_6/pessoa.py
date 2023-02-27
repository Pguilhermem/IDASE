class Pessoa:
    def __init__(self, nome, idade):
        self.set_nome(nome)
        self.set_idade(idade)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser uma string.")
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        if not isinstance(idade, int) or idade < 0:
            raise ValueError("A idade deve ser um número inteiro positivo.")
        self.__idade = idade