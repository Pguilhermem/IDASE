# inicializa as variáveis
ingressos_vendidos = 0
preco_ingresso = 50

# loop para permitir que os usuários comprem ingressos
while True:
    # verifica se há ingressos disponíveis
    if ingressos_vendidos >= 100:
        print("Desculpe, todos os ingressos já foram vendidos.")
        break

    # pede ao usuário a quantidade de ingressos desejados
    quantidade = int(input("Quantos ingressos você deseja comprar? "))

    # verifica se a quantidade é válida
    if quantidade <= 0:
        print("Quantidade inválida. Tente novamente.")
        continue

    # calcula o preço total dos ingressos
    preco_total = quantidade * preco_ingresso

    # verifica se o usuário tem direito ao desconto
    if quantidade >= 10:
        preco_total *= 0.9

    # verifica se há ingressos suficientes para a compra
    if ingressos_vendidos + quantidade > 100:
        print("Desculpe, não há ingressos suficientes para essa compra. Há apenas",
              100 - ingressos_vendidos, "ingressos restantes.")
        continue

    # atualiza o número de ingressos vendidos e exibe o preço total
    ingressos_vendidos += quantidade
    print("O preço total da sua compra é:", preco_total)

print("Fim do programa.")
