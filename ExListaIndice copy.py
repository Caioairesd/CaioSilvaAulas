
clientes = ["Caio","Eberth","Daniel","Kaio","Rafael",]
telefone = ["4711111111","4722222222","4733333333","4744444444","4755555555",]
bairro = ["Adhemar Garcia","Itaum","Paranaguamirim","Comasa","Comasa",]

ClientesRequest = input("Insira o nome do cliente:")
if ClientesRequest in clientes:
    i = clientes.index(ClientesRequest)
    nome = clientes[i]
    tel = telefone[i]
    end = bairro[i]
    print("O cliente {} de telefone {} mora no bairro {}".format(nome),(tel),(end))
else:
    print("{} Não existe na base de dados".format(ClientesRequest))


