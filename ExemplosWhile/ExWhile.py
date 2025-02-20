venda = input("Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter sem digitar nada:")
vendas = []

#CRIE UM PROGRAMA 
while venda != "":
    vendas.append(venda)
    venda = input("Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter sem digitar nada:")
print("Rgeistro Finalizado! As vendas cadastradas foram: {}".format(vendas))