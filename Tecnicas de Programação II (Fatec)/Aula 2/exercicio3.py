#3) Segundo uma tabela médica, o peso ideal está relacionado com a altura e o sexo. Elabore um algoritmo em Python que leia a altura e o sexo de uma pessoa, calcule e mostre o seu peso ideal, utilizando as seguintes fórmulas. Para homens: (72.7*altura)–58 Para mulheres: (62.1*altura)–44.

# Entrada de dados
altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (M para masculino ou F para feminino): ")

# Verificação do sexo
if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
    print("O peso ideal para homens com {:.2f} metros de altura é {:.2f} kg.".format(altura, peso_ideal))
elif sexo.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print("O peso ideal para mulheres com {:.2f} metros de altura é {:.2f} kg.".format(altura, peso_ideal))
else:
    print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")
