# Você está criando um aplicativo de entrega de comida e precisa calcular o preço final do pedido do usuário.
#O usuário escolheu alguns itens do cardápio e é preciso calcular o preço total do pedido.


valorHamburguer = float(input("Digite o valor unitário do hambúrguer: "))
quantidadeHamburguer = int(input("Digite a quantidade de hambúrgueres desejada: "))
valorBebida = float(input("Digite o valor unitário da bebida: "))
quantidadeBebida = int(input("Digite a quantidade de bebidas desejada: "))
valorPago = float(input("Digite o valor pago pelo usuário: "))

# Cálculo do preço total dos hambúrgueres e da bebida
preco_total_hamburgueres = 10.00 * 2
preco_total_bebida = 5.00 * 1

# Cálculo do preço total do pedido
preco_total_pedido = 20.00 + 5.00

# Cálculo do troco necessário
troco_necessario =  30.00 - 25.00 

# Impressão do resultado
mensagem = f"O preço final do pedido é R$ {preco_total_pedido:.2f}. Seu troco é R$ {troco_necessario:.2f}."
print(mensagem)