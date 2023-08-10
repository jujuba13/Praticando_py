##identificar rapidamente os pedidos veganos e não veganos e informar as calorias de cada prato definido
# pelo cliente

# Função para obter a descrição do tipo de prato (vegano ou não)
def get_tipo_prato(vegano):
    return "Vegano" if vegano else "Não-vegano"

# Entrada do número de pedidos
n = int(input("Digite o número de pedidos: "))

pedidos = []

# Coleta de informações de cada pedido
for i in range(n):
    nome_prato = input(f"Digite o nome do prato do pedido {i + 1}: ")
    calorias = int(input(f"Digite a quantidade de calorias do prato do pedido {i + 1}: "))
    eh_vegano = input(f"O prato do pedido {i + 1} é vegano? (s/n): ").lower() == "s"
    
    pedidos.append((nome_prato, calorias, eh_vegano))

# Exibição da lista de pedidos com suas informações
print("Lista de pedidos:")
for i, pedido in enumerate(pedidos, start=1):
    nome_prato, calorias, eh_vegano = pedido
    tipo_prato = get_tipo_prato(eh_vegano)
    print(f"Pedido {i}: {nome_prato} ({tipo_prato}) - {calorias} calorias")
