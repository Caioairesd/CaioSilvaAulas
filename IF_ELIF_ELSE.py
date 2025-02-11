meta = 20000
vendas = 25000

if vendas < meta:
    print("Não ganhou bônus.")
elif vendas >(meta*2):
    bonus = 0.07 * vendas
    print("Ganhou {} de bonus".format(bonus))
else:
    bonus = 0.03 * vendas
    print("Ganhou {} de bônus".format(bonus))