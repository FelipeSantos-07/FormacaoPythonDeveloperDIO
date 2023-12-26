'''
< OPERADORES DE IDENTIDADE >
Utilizados para comparar se dois objetos testados ocupam a mesma posição de memória

    is: operador de identidade para confirmar se os dados são iguais
    is not: para confirmar se eles não são iguais
'''

curso = "Curso de Python"
nomeCurso = curso
saldo, limite = 200, 200

print(curso is nomeCurso)
print(curso is not nomeCurso) # Dá falso pois ambos utilizam a mesma posição na memória
print(saldo is limite)