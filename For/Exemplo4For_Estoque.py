estoque = [100,50,80,190,200,210,45,37,99,105,130]
produtos = ['RTX 4060','GTX 1650','RX 580','RTX 4090','B500 AORUS ELITE','B450','MEMORIA RAM','SSD KINGSTON 1TB','FONTE MANCER 500W','TECLADO PICHAU','HEADSET REDRAGON']
nivelMinimo = 50 

for i ,  qtde in enumerate (estoque):

    if qtde < nivelMinimo:
        
        print(produtos[i],qtde)