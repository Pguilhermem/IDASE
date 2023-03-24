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
        except Exception as __e:
            print(
                f"Dados recebidos no construtor são inconsistentes. Erro: {__e}")
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
