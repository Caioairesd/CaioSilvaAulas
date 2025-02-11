#Acão para ver todos os metodos possíves print(dir(str)).


#Transforma apenas a primeira letra de uma string em maiuscula.
nome = "caio"
print(nome.capitalize(),"\n")

#Transforma todas as letras em minusculas.
nome = "CAIO"
print(nome.casefold(),"\n")



#Conta o número de vezes que um caractere especifico aparece na String.
#Case sensitive.
nome = "CaioVinicius@gmail.com" 
print(nome.count("i"),"\n")


#Retorna true ou false PARA UM TESTE se A STRING TERMINA COM UMA STRING ESPECIFICA. 
nome = "CaioVinicius@gmail.com" 
print(nome.endswith("gmail.com"),"\n")


#Encontra a posição do termo procurado. Lembre-se começa do zero.
nome = "CaioVinicius@gmail.com" 
print(nome.find("@"),"\n")


#Verifica se o texto é todo feito com letras.
nome = "Caio" 
print(nome.isalpha(),"\n")


#Verifica se o texto é feito de números. 
nome = '123'
print(nome.isnumeric(),"\n")


#Substitue  um caractere escolhido por outro.
nome = "Caio" 
print(nome.replace("C","K"),"\n")
 
 
#Separa o TEXTO string baseado em algum caractere indicado.
nome = "Caio @ Kaio" 
print(nome.split("@"),"\n")


#Coloca todas as letras iniciais em maisculas.
nome = "caio vinicius aires da silva"
print(nome.title(),"\n")


#Retira os caracteres indesejados, como por exemplo espaços que não agregam valor.
nome = "   Caio Vinicius Aires da Silva"
print(nome.strip(),"\n")


#Retorna true OU false para um teste de uma string se inicia com um texto especifico.
#Case sensitive.
nome = "Caio 1910"
print(nome.startswith("Cai"),"\n")
print(nome.startswith("cai"),"\n")