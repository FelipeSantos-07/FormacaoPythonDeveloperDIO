'''
< OPERADORES LÓGICOS > 
- Utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica
  Expressão = operadorComparação + operadorLógico + operadorComparação + operadorLógico + ...

- Tipos de operadores:
    and: para ser verdadeiro, as duas sentenças precisam ser verdadeiras
    or: para ser verdadeiro, apenas uma das sentenças precisam ser verdadeiras
    not: inverte o sentido da afirmação (True -> False e False -> True)
'''

# EXEMPLO
saldo = 1000
saque = 200
limite = 100

print('1a verificação: ', saldo >= saque)
print('2a verificação: ', saque <= limite)

# OPERADOR E (and)
print('\nAND: ', saldo >= saque and saque <= limite)

# OPERADOR OU (or)
print('OR: ', saldo >= saque or saque <= limite)

# OPERADOR DE NEGAÇÃO (not)
print("\n1000 é maior que 1500?\nR:", not 1000 > 1500)
print("\nTemos alguma string?\nR:", not "Saque 1500/")

# PARÊNTESES
# Um sistema bancário não pode permitir que uma pessoa retire um valor que ela não tenha e que seja maior que o limite ou se a pessoa tiver uma conta especial, com o saldo dentro da conta bancária
saldo = 1000
saque = 250
limite = 200
contaEspecial = True

print("\n\nÉ possível realizar o saque?\nR:", (saldo >= saque and saque <= limite) or (contaEspecial and saldo >= saque))