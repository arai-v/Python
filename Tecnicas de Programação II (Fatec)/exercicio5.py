#5) ESCREVER UM ALGORITMO EM PYTHON PARA LER O CUSTO DE FABRICAÇÃO DE UM CARRO, O CUSTO DE UM CARRO NOVO AO CONSUMIDOR É A SOMA DO CUSTO DE FÁBRICA COM A PORCENTAGEM DO DISTRIBUIDOR E A PORCENTAGEM DOS IMPOSTOS. SUPONDO QUE O PERCENTUAL DO DISTRIBUIDOR SEJA DE 28% E OS IMPOSTOS DE 45% EM CIMA DO CUSTO DE FABRICAÇÃO. CALCULE E ESCREVA O CUSTO FINAL AO CONSUMIDOR.

# Entrada de dados
custo_fabricacao = float(input("Digite o custo de fábrica do carro: "))

# Cálculo do custo final ao consumidor
percentual_distribuidor = 0.28
percentual_impostos = 0.45
custo_final = custo_fabricacao + (custo_fabricacao * percentual_distribuidor) + (custo_fabricacao * percentual_impostos)

# Saída de dados
print("Custo final ao consumidor: R$", custo_final)