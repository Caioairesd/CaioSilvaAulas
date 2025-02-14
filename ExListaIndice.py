produtos = ["tv","celular","mouse","teclado,","Tablet"]

vendas = [1000,1500,350,278,900]

print("As vendas de {} foram de {}".format(produtos[1],vendas[1]))
 
 
i = produtos.index("mouse")
print("O valor de i é "+ str(i))

print("O produto da posição i é "+ str(i))








produtos = ["tv","celular","mouse","teclado","Tablet","geladeira"]

estoque = [100,150,100,120,70,180,80]

produto = input("Insira o nome do produto:")
if produto in produtos:
    i = produtos.index(produto)
    qtdeEstoque = estoque[i]
    print("Temos {} unidades de {} no estoque".format(qtdeEstoque,(produto)))
else:
    print("{} Não existe no estoque".format(produto))


