def getData():

    nomeUsuario = input("Escreva seu nome: ")
    idadeUsuario = int(input("Qual a sua idade? "))

    tuplaData = (nomeUsuario, idadeUsuario)
    return tuplaData


def mensagem(nomeUsuario,idadeUsuario):

    if idadeUsuario <= 10:
        print("Oi",nomeUsuario)
    else:
        print("Olá",nomeUsuario)

def main():
    nomeUsuario,idadeUsuario = getData()
    mensagem(nomeUsuario,idadeUsuario)

main()


