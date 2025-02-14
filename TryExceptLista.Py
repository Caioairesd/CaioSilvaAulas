
produtos = ["tv","celular","mouse","teclado","Tablet","geladeira"]
ItemUser = input('Qual item você deseja remover')
try:
    produtos.reomove(ItemUser)
    print(produtos)
except:
    print('O produto {} não xiste na lista'.format(ItemUser))
