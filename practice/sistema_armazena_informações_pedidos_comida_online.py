##O sistema deve permitir ao cliente inserir novos pedidos, escolher um cupom de desconto (10% ou 20%) 
#e exibir o valor total de todos os pedidos realizados até o momento, com o desconto aplicado.



# Função para calcular o valor total com desconto
def calcular_valor_total(pedidos, desconto):
    total = sum([valor for valor in pedidos])
    desconto_percentual = desconto / 100
    valor_com_desconto = total * (1 - desconto_percentual)
    return valor_com_desconto

# Entrada
n = int(input())
pedidos = []
for _ in range(n):
    nome_pedido, valor_pedido = input().split()
    pedidos.append((nome_pedido, float(valor_pedido)))

cupom_desconto = int(input())

# Cálculo do valor total com desconto
desconto = 0
if cupom_desconto == 10:
    desconto = 10
elif cupom_desconto == 20:
    desconto = 20

valor_com_desconto = calcular_valor_total(pedidos, desconto)

# Saída
print(f"Valor total: {valor_com_desconto:.2f}")
