from pessoa import Pessoa


joao = Pessoa("João", 30)

try:
    joao.set_nome("João Silva")
    joao.set_idade(31)
    maria = Pessoa("Maria", 25)
except Exception as e:
    print(e)

joao.imprime_dados()
maria.imprime_dados()
