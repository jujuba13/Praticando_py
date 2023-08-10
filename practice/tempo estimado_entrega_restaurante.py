## informar ao usuário o tempo estimado de entrega de um restaurante. 
##A mensagem deve conter o nome do restaurante e o tempo estimado de entrega em minutos.

nomeRestaurante = input("Digite o nome do restaurante: ")
tempoEstimadoEntrega = int(input("Digite o tempo estimado de entrega em minutos: "))

mensagem = f"O restaurante {nomeRestaurante} entrega em {tempoEstimadoEntrega} minutos."
print(mensagem)
