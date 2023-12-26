'''
< ESTRUTURAS CONDICIONAIS >
Permite o desvio do fluxo de controle quando determinada CONDIÇÃO é verdadeira
'''

# IF / IF-ELSE / ELIF
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")

# IF ANINHADO
# É quando eu coloco uma estrutura condicional dentro de outra

# IF TERNÁRIO
# Quando escrevo a condição em uma única linha
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
