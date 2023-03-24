"""
Módulo que possui as classes 
Pessoa
Estudante
Trabalhador
"""


class Pessoa:
    """
    Classe que define uma pessoa
    atributos: nome e idade
    métodos: get_nome, get_idade, set_nome e set_idade
    """

    def __init__(self, nome, idade):
        """
        Construtor da classe pessoa
        :param nome: nome que será atribuído à pessoa
        :param idade: idade que será atribuída à pessoa
        """
        try:
            self.set_nome(nome)
            self.set_idade(idade)
        except Exception as _e:
            print(
                f"Dados recebidos no construtor são inconsistentes. Erro: {_e}")
            self.__nome = ""
            self.__idade = 0

    def get_nome(self):
        """
        Método get para a obtenção do nome da pessoa
        """
        return self.__nome

    def set_nome(self, nome):
        """
        Método para alteração do nome
        :param nome: str
        """
        if not isinstance(nome, str):
            raise TypeError(
                "O nome deve ser uma string. Alteração do nome não realizada")
        self.__nome = nome

    def get_idade(self):
        """
        Método get para a obtenção da idade da pessoa
        """
        return self.__idade

    def set_idade(self, idade):
        """
        Método para alteração da idade
        :param idade: int positivo
        """
        if not isinstance(idade, int) or idade < 0:
            raise ValueError(
                "A idade deve ser um número inteiro positivo. Alteração da idade não realizada.")
        self.__idade = idade

    def imprime_dados(self):
        """
        Método que imprime na tela os dados de uma pessoa
        """
        print(f"Nome: {self.__nome} | Idade: {self.__idade}")

    def falar(self):
        """
        Método que imprime na tela uma mensagem da pessoa
        """
        print(
            f"Olá, meu nome é {self.get_nome()} e tenho {self.get_idade()} anos.")


class Estudante(Pessoa):
    """
    Classe Estudante, que é uma versão especializada da classe Pessoa
    """

    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        try:
            self.set_curso(curso)
        except Exception as _e:
            print(
                f"Dados recebidos no construtor são inconsistentes. Erro: {_e}")
            self.__curso = ""

    def get_curso(self):
        """
        Método get para a obtenção do curso da pessoa
        """
        return self.__curso

    def set_curso(self, curso):
        """
        Método para alteração do curso
        :param curso: str
        """
        if not isinstance(curso, str):
            raise TypeError(
                "O curso deve ser uma string. Alteração do curso não realizada")
        self.__curso = curso

    def falar(self):
        """
        Método que imprime na tela uma mensagem do estudante
        """
        super().falar()
        print(f"Eu faço {self.get_curso()}.")


class Trabalhador(Pessoa):
    """
    Classe Empresa, que é uma versão especializada da classe Pessoa
    """

    def __init__(self, nome, idade, empresa):
        super().__init__(nome, idade)
        try:
            self.set_empresa(empresa)
        except Exception as _e:
            print(
                f"Dados recebidos no construtor são inconsistentes. Erro: {_e}")
            self.__empresa = ""

    def get_empresa(self):
        """
        Método get para a obtenção da empresa em que a pessoa trabalha
        """
        return self.__empresa

    def set_empresa(self, empresa):
        """
        Método para alteração do empresa
        :param empresa: str
        """
        if not isinstance(empresa, str):
            raise TypeError(
                "A empresa deve ser uma string. Alteração da empresa não realizada")
        self.__empresa = empresa

    def falar(self):
        """
        Método que imprime na tela uma mensagem do trabalhador
        """
        super().falar()
        print(f"Sou um trabalhador da empresa {self.get_empresa()}.")
