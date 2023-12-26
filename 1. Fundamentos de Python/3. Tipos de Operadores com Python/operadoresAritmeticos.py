'''
< OPERADORES ARITMÉTICOS >
Servem para realizar operações matemáticas: soma, subtração, multiplicação e divisão

- É levado em conta a precedência das operações: P.E.M.D.A.S (Entre M-D e A-S segue-se a regra da esquerda para a direita)
'''

num1, num2 = int(input('- Digite um número: ')), int(input('- Digite outro número: '))
print(f'\nOPERAÇÕES ARITMÉTICAS ENTRE {num1} E {num2}')

# ADIÇÃO (+)
print('> Soma: ', num1 + num2)

# SUBTRAÇÃO (-)
print('> Subtração: ', num1 - num2)

# MULTIPLICAÇÃO (*)
print('> Multiplicação: ', num1 * num2)

# DIVISÃO COMUM, com decimal (/)
print('> Divisão comum: ', num1 / num2)

# DIVISÃO INTEIRA (//)
print('> Divisão inteira: ', num1 // num2)

# MÓDULO, ou resto da divisão (%)
print('> Módulo/Resto da divisão: ', num1 % num2)

# EXPONENCIAÇÃO, ou elevado à (**)
print('> Exponenciação: ', num1 ** num2)