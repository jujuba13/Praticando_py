##Crie um programa que informe ao usuário se ele pode receber um brinde especial de acordo com o valor total 
##do pedido.

valorPedido = float(input("Digite o valor total do pedido: "))

if valorPedido >= 50.00:
    mensagem = "Parabéns, você ganhou uma sobremesa grátis!"
else:
    mensagem = "Que pena, você não ganhou nenhum brinde especial."

print(mensagem)
