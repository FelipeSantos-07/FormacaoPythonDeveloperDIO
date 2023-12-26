'''
< A ESTÉTICA >
A indentação do código, além de deixá-lo mais legível (separando em blocos), ele faz com que o interpretador identifique onde começa e termina um bloco de comando
'''

def sacar(valor:float): # Inicia o bloco da função
    saldo = 500.00

    if saldo >= valor: # Inicia o bloco do if
        saldo -= valor
        print(f"Saque: R${valor:.2f}\nSaldo atual: R${saldo:.2f}")
        
    # Termina o bloco do if

# Termina o bloco da função
sacar(490)