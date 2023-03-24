from pessoas import Pessoa, Estudante, Trabalhador

joao = Pessoa("João", 30)
jose = Estudante("José", 23, "Engenharia")
manoel = Trabalhador("Manoel", 40, "Petrobrás")


lista_pessoas = [joao, jose, manoel]

for p in lista_pessoas:
    p.falar()
