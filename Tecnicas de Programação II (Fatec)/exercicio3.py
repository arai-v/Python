#3) FAÇA UM PROGRAMA EM PYTHON QUE LEIA UMA TEMPERATURA EM GRAUS CELSIUS E CONVERTA-A PARA GRAUS FAHRENHEIT. A FÓRMULA DE CONVERSÃO É: F = C * 1.8 + 32 SENDO F A TEMPERATURA EM FAHRENHEIT E C A TEMPERATURA EM CELSIUS.

# Entrada de dados
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))

# Cálculo da temperatura em Fahrenheit
temperatura_fahrenheit = (temperatura_celsius * 1.8) + 32

# Saída de dados
print("Temperatura em graus Fahrenheit:", temperatura_fahrenheit)