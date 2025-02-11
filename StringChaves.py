#Format normal
faturamento = 2000 
custo = 500
lucro = faturamento - custo
print("O faturamento da loja foi de: {}".format(faturamento) )



faturamento = 2000 
custo = 500
lucro = faturamento - custo
print("O faturamento da loja foi de: {}. O custo foi de: {}. e o lucro foi de: {}".format(faturamento,custo,lucro) )


#Buscando as variáveis por posição
faturamento = 2000 
custo = 500
lucro = faturamento - custo
print("O faturamento da loja foi de: {0}. O custo foi de: {1}. e o lucro foi de: {2}".format(faturamento,custo,lucro) )


#String
faturamento = 2000 
custo = 500
lucro = faturamento - custo
print("O faturamento da loja foi de: %s" % faturamento)


#Int
faturamento = 2000 
custo = 500
lucro = faturamento - custo
print("O faturamento da loja foi de: %d" % faturamento)


#Uso do in, retorna true se o valor estiver contido na sequência 
email = "CaioVinicius@gmail.com"

print("@" in "Vinicius@gmail.com")


#Se não tiver contido na sequência retorna False
email = "CaioVinicius@gmail.com"

print("@" in "Vinicius.gmail.com")