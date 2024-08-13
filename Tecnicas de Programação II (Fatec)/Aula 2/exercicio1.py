#1) Faça um codigo em python que leia dois números e calcule a divisão do maior número pelo menor número.

# Entrada de dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Verificação do maior e menor número
if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1

# Cálculo da divisão
divisao = maior / menor

# Saída de dados
print("A divisão do maior número pelo menor número é:", divisao)