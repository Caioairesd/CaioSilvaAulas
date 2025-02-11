#Faça um programa que receba uma nota do aluno e
#se for superior ou igual a 7 apareça mensagem que 
#ele está aprovado, se for inferior a 5 
#"Não aprovado/reprovado direto" e se estiver entre 5 e 7 
#apareça a mensagem "Não aprovado/recuperação"

nota = float(input("Insira sua nota:"))

if nota >= 7:
    print("Aluno aprovado!")
else:
    if nota <= 5:
        print("Aluno reprovado.")
    else: 
        print("Aluno de recuperação.")
