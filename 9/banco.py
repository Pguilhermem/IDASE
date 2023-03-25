from contas import Conta, ContaCorrente, ContaPoupanca


class Banco():
    """
    Classe Banco
    """

    def __init__(self, senha_gerente):
        """
        Construtor da Classe Banco
        :param senha_gerente: Senha do Gerente
        """
        self.__senha_gerente = senha_gerente
        self._contas = []

    def _busca_conta(self, num):
        for conta in self._contas:
            if conta.numero == num:
                return conta
        print("Número de conta inválido ou conta inexistente")
        return None

    def atendimento(self):
        """
        Realiza o atendimento do Banco
        """
        op = 1
        print("Sistema de atendimento bancário")
        while op == 1 or op == 2:
            try:
                op = int(input(
                    "Selecione a opção desejada:\r\n1) Atendimento cliente\r\n2) Atendimento gerente\r\n3) Sair : "))
                if op == 2:
                    self.atendimento_gerente()
                elif op == 1:
                    self.atendimento_cliente()
                elif op == 3:
                    break
                else:
                    pass
            except Exception as e:
                print("Erro no menu de atendimento", e.args)

    def atendimento_cliente(self):
        """
        Realiza o Atendimento do Cliente
        """
        atendimento = True
        while atendimento:
            conta_usuario = None
            while conta_usuario is None:
                try:
                    print("Atendimento ao cliente")
                    num_conta_usuario = input(
                        "Digite o Numero de sua Conta (q para sair): ")
                    conta_usuario = self._busca_conta(int(num_conta_usuario))
                except Exception as e:
                    if num_conta_usuario == 'q':
                        return
                    else:
                        print(f"Erro na busca de dados da conta: {e.args}")

            senha_usuario = int(input("Digite sua senha: "))
            if (conta_usuario.valida_senha(senha_usuario)):
                print(f"Bem vindo ao sistema Sr(a). {conta_usuario.titular}")
                op = 0
                while op != 6:
                    try:
                        op = int(input(
                            "Digite a opção desejada: 1) Ver Saldo 2) Realizar Saque 3) Realizar Depósito 4) Simular Rendimentos 5) Ver número do cartão de crédito 6) Sair: "))
                        if op == 1:
                            print(
                                f'Seu saldo é de: R${conta_usuario.get_saldo(senha_usuario)}')
                        elif op == 2:
                            conta_usuario.saque(senha_usuario, int(
                                input("Digite o valor do saque: ")))
                        elif op == 3:
                            conta_usuario.deposito(
                                int(input("Digite o valor do depósito: ")))
                        elif op == 4:
                            if isinstance(conta_usuario, ContaPoupanca):
                                conta_usuario.simula_rendimentos(
                                    int(input("Digite o número de meses: ")))
                            else:
                                print("Esta conta não é do tipo poupança")
                        elif op == 5:
                            if isinstance(conta_usuario, ContaCorrente):
                                print("Número do cartão do usuário: ",
                                      conta_usuario.get_num_cartao(senha_usuario))
                            else:
                                print("Esta conta não é do tipo corrente")
                        else:
                            pass
                    except Exception as e:
                        print("Erro no atendimento ao cliente: ", e.args)

    def atendimento_gerente(self):
        """
        Realiza o atendimento do gerente
        """
        if self.valida_senha(int(input("Digite a senha de gerente: "))):
            op = 0
            while op != 2:
                try:
                    op = int(
                        input("Digite a operacao desejada: 1) Cadastrar uma nova conta 2) Sair: "))
                    if int(op) == 1:
                        tipo = input(
                            "Digite o tipo de conta: 1) Poupança 2) Corrente: ")
                        if tipo == '1':
                            nc = self.cadastra_conta(input("Digite o Titular da Conta: "), senha=int(input("Digite a senha da conta: ")), saldoi=float(
                                input("Digite o saldo inicial da conta: ")), taxa=float(input("Digite a taxa de juros: ")))
                        elif tipo == '2':
                            nc = self.cadastra_conta(input("Digite o Titular da Conta: "), senha=int(input("Digite a senha da conta: ")), saldoi=float(
                                input("Digite o saldo inicial da conta: ")), ncartao=input("Digite o número do cartão: "))
                        else:
                            print("Opção Inválida")
                            continue
                        print(f"Conta {nc} cadastrada!")
                    elif int(op) == 2:
                        return
                    else:
                        print("Opção Inválida")
                        continue
                except Exception as e:
                    print("Erro no atendimento ao gerente: ", e.args)
        else:
            print("Senha do gerente inválida")

    def cadastra_conta(self, titular, senha, saldoi=0.0, taxa=None, ncartao=None) -> int:
        """
        Cadastra contas novas
        :param titular: nome do titular
        :param senha: senha da conta
        :param saldoi: saldo inicial para a conta
        """
        num_conta_nova = len(self._contas)+1
        if taxa is not None:
            c = ContaPoupanca(num_conta_nova, titular, senha, taxa, saldoi)
        elif ncartao is not None:
            c = ContaCorrente(num_conta_nova, titular, senha, ncartao, saldoi)
        else:
            raise ValueError("Deve-se informar no número do cartão ou a taxa")
        self._contas.append(c)
        return num_conta_nova

    def valida_senha(self, senha_gerente):
        """
        Valida a senha de gerente
        :param senha_gerente: senha do gerente
        """
        if self.__senha_gerente == senha_gerente:
            return True
        else:
            return False
