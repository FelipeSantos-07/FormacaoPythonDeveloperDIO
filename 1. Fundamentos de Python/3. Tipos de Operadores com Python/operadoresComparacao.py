'''
< OPERADORES DE COMPARAÇÃO >
Utilizados para comparar dois valores

- Igualdade: analisa se dois valores são iguais
- Diferença: analisa se dois valores são diferentes
- Maior/Maior ou igual: verifica se o primeiro valor é maior (ou igual) que o segundo
- Menor/Menor ou igual: verifica se o primeiro valor é menor (ou igual) que o segundo
'''

# VARIÁVEIS PARA COMPARAÇÃO
saldo, saque = 450, 200

print(f'COMPARAÇÃO ENTRE O SALDO (R$ {float(saldo)}) E O SAQUE (R$ {float(saque)})')

# IGUALDADE (==)
print('> IGUALDADE: ', saldo == saque)

# DIFERENÇA (!=)
print('> DIFERENÇA: ', saldo != saque)

# MAIOR QUE (>)
print('> MAIOR QUE: ', saldo > saque)

# MAIOR OU IGUAL QUE (>=)
print('> MAIOR OU IGUAL QUE: ', saldo >= saque)

# MENOR QUE (<)
print('> MENOR QUE: ', saldo < saque)

# MENOR OU IGUAL QUE (<=)
print('> MENOR OU IGUAL QUE: ', saldo <= saque)