#Faça um programa que o usuário digita um número e diga se o número é superior a 20,
#inferiro a 10 ou se está entre 10 e 20.

numero = float(input("Insira o número:"))
if numero > 20:
    print("O número é superior a 20.")
elif numero < 10:
    print("O número é inferior a 10.")
else:
    print("O número está entre 10 e 20.")