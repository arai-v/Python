#4) FAÇA UM ALGORITMO EM PYTHON QUE LEIA O ANO DE NASCIMENTO DE UMA PESSOA, E LEIA O NOME DA PESSOA E ESCREVA QUANTOS ANOS ESSA PESSOA TEM , E MOSTRE O NOME DIGITADO.

# Entrada de dados
ano_nascimento = int(input("Digite o ano de nascimento: "))
nome_pessoa = input("Digite o nome da pessoa: ")

# Cálculo da idade
ano_atual = 2024  # ou podemos usar datetime.now().year para obter o ano atual
idade = ano_atual - ano_nascimento

# Saída de dados
print("Nome:", nome_pessoa)
print("Idade:", idade, "anos")