#2) Construa um programa em Python que receba o nome e peso de duas pessoas e diga qual a pessoa mais pesada, e verifica se as pessoas tem o mesmo peso.

# Entrada de dados
nome1 = input("Digite o nome da primeira pessoa: ")
peso1 = float(input("Digite o peso da primeira pessoa: "))

nome2 = input("Digite o nome da segunda pessoa: ")
peso2 = float(input("Digite o peso da segunda pessoa: "))

# Verificação do peso
if peso1 > peso2:
    print("A pessoa mais pesada é {} com {:.2f} kg.".format(nome1, peso1))
elif peso2 > peso1:
    print("A pessoa mais pesada é {} com {:.2f} kg.".format(nome2, peso2))
else:
    print("As duas pessoas têm o mesmo peso de {:.2f} kg.".format(peso1))
