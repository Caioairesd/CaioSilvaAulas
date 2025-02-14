faturamento = input("Qual foi o faturamento da loja esse mês?")
custo = input("Qual foi o custo da loja esse mês?")
if faturamento =="" and custo == "":
    print("Campos não preenchidas!")
else:
    lucro = int(input(faturamento) - int(custo))
    print("O lucro foi de {}R$" .format(lucro))