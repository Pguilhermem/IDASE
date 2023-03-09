from pessoa import Pessoa

# Criando um objeto Pessoa
p = Pessoa("João", 30)

# Obtendo o nome e a idade da pessoa
print(p.get_nome()) # Saída: "João"
print(p.get_idade()) # Saída: 30

# Tentando atribuir um novo nome inválido
try:
    p.set_nome(123)
except TypeError as e:
    print(e) # Saída: "O nome deve ser uma string."

# Tentando atribuir uma nova idade inválida
try:
    p.set_idade(-10)
except ValueError as e:
    print(e) # Saída: "A idade deve ser um número inteiro positivo."

# Atribuindo um novo nome e idade válidos
p.set_nome("Maria")
p.set_idade(25)

# Obtendo o novo nome e idade da pessoa
print(p.get_nome()) # Saída: "Maria"
print(p.get_idade()) # Saída: 25

# Tentando atribuir um novo nome inválido
try:
    p.set_nome(123)
except TypeError as e:
    print(e) # Saída: "O nome deve ser uma string."

# Tentando criar um objeto com dados inválidos
try:
    p = Pessoa(345,-10)
except Exception as e:
    print(e)
