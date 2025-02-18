PessoasPresentes = ['Caio Vinicius','Eberth Rodrigues','Kaio Mazza','Daniel Balera','Eduardo Alibaba']

chamada = 'Eduardo Alibaba'

for pessoa in PessoasPresentes:
    if pessoa == chamada:
        print("{} Está presente".format(chamada))
        break
    else:
        print("Só um print para mostrar que o for já passou por essa pessoa:"+str(pessoa))
        continue
        print("Só para mostrar que não aparece")