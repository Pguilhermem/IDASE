#Exibindo os elementos de uma tupla
tupla = (1, 2, 3, 4, 5)
print(tupla)

#Acessando elementos de uma lista 
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primeiro_elemento = lista[0]
ultimo_elemento = lista[-1]
print(primeiro_elemento, ultimo_elemento)

#Acessando uma sublista -> lista[início:fim:passo]
sublista1 = lista[1:8:2]
print(sublista1)

sublista2 = lista[10:2:-2]
print(sublista2)

sublista3 = lista[10::-1]
print(sublista3)

#Modificando elementos de uma lista
lista = [1, 2, 3, 4, 5]
lista[0] = 10
print(lista)


#Exibindo os elementos de um dicionário
dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print(dicionario)

#Acessando elementos de um dicionário
dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
idade = dicionario["idade"]
print(idade)

#Modificando elementos de um dicionário
dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
dicionario["idade"] = 40
print(dicionario)

#Exibindo os elementos de um conjunto
conjunto = {1, 2, 3, 4, 5}
print(conjunto)

#Adicionando elementos em um conjunto
conjunto = {1, 2, 3}
conjunto.add(4)
print(conjunto)

#Removendo elementos de um conjunto
conjunto = {1, 2, 3, 4}
conjunto.remove(4)
print(conjunto)

#Usando métodos de conjunto para realizar operações em conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
uniao = conjunto1.union(conjunto2)
intersecao = conjunto1.intersection(conjunto2)
diferenca = conjunto1.difference(conjunto2)
print("União:", uniao)
print("Interseção:", intersecao)
print("Diferença:", diferenca)