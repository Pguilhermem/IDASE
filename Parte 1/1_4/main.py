from functools import reduce


# Exemplo de map() : aplica uma função a cada elemento de uma sequência e retorna um iterador com os resultados.
numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x ** 2, numbers)
print(list(squares))  # Saída: [1, 4, 9, 16, 25]

# Exemplo de filter(): cria uma lista com os elementos de uma sequência que atendem a uma determinada condição.
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Saída: [2, 4]

# Exemplo de reduce(): aplica uma função a uma sequência de elementos de maneira cumulativa, de forma que o resultado é reduzido a um único valor.
numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)  # Saída: 15

# Exemplo de sorted(): ordena uma sequência de elementos em ordem crescente/decrescente de acordo com uma função de chave
words = ['apple', 'banana', 'cherry', 'date']
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words)  # Saída: ['date', 'apple', 'banana', 'cherry']

# Exemplo de any(): verifica se pelo menos um elemento de uma sequência é True
values = [False, False, True, False]
print(any(values))  # Saída: True

# Exemplo de all(): verifica se todos os elementos de uma sequência são True.
values = [True, True, False, True]
print(all(values))  # Saída: False

# Exemplo de zip(): combina duas ou mais sequências em tuplas
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
zipped_data = zip(names, ages)
# Saída: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
print(list(zipped_data))

# Exemplo de enumerate(): retorna um iterador de tuplas que associa um índice a cada elemento de uma sequência
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(i, fruit)
# Saída:
# 0 apple
# 1 banana
# 2 cherry

# Exemplo de max(): retorna o maior elemento de uma sequência.

numbers = [1, 5, 2, 4, 3]
print(max(numbers))  # Saída: 5

# Exemplo de min(): retorna o menor elemento de uma sequência.

numbers = [1, 5, 2, 4, 3]
print(min(numbers))  # Saída: 1

# Exemplo de sum(): retorna a soma dos elementos de uma sequência.
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # Saída: 15
