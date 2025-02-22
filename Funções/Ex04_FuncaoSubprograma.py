def getName():
    nomeUsuario = input("Insira o seu nome: ")
    return nomeUsuario

def printMensagem(nomeUsuario):
    print("Olá jovem padawan!",nomeUsuario)

def main():
    nomeUsuario = getName()
    printMensagem(nomeUsuario)

main()