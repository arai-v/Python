#1) UMA EMPRESA DE DESENVOLVIMENTO DE SOFTWARES PAGA A SEU VENDEDOR UM FIXO DE R$1500 POR MÊS, MAIS UM BÔNUS DE R$50 POR SOFTWARE VENDIDO. FAÇA UM ALGORITMO EM PYTHON QUE LEIA A QUANTIDADE DE SOFTWARES VENDIDOS E CALCULE O SALÁRIO TOTAL DO FUNCIONÁRIO

# Entrada de dados
quantidade_softwares = int(input("Digite a quantidade de softwares vendidos: "))

# Cálculo do salário total
salario_fixo = 1500
bonus_por_software = 50
salario_total = salario_fixo + (quantidade_softwares * bonus_por_software)

# Saída de dados
print("Salário total: R$", salario_total)