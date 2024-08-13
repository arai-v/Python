#2) ANALISANDO A FORMULA: VALORATRASO = VALOR + (VALOR * (TAXA/100) * TEMPO), CRIE UM ALGORITMO EM PYTHON PARA EFETUAR O CALCULO DO VALOR DE UMA PRESTAÇÃO EM ATRASO. LEIA O VALOR DA PRESTAÇÃO E A TAXA DE JUROS IMPOSTA PELO BANCO, E LEIA A QUANTIDADE DE MESES EM ATRASO. (TEMPO)

# Entrada de dados
valor_da_prestacao = float(input("Digite o valor da prestação: "))
taxa_de_juros = float(input("Digite a taxa de juros (em porcentagem): "))
tempo_em_atraso = int(input("Digite a quantidade de meses em atraso: "))

# Cálculo do valor da parcela em atraso
valor_atraso = valor_da_prestacao + (valor_da_prestacao * (taxa_de_juros/100) * tempo_em_atraso)

# Saída de dados
print("Valor da parcela em atraso: R$", valor_atraso)