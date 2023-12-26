'''
< OPERADORES DE ASSOCIAÇÃO >
Para verificar se um objeto está em uma sequência

    in: para verificar se algo está em alguma sequência (case sensitive)
    not in: para confirmar se algo não está em uma sequência
'''

curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

print("Python" in curso) # Verificar se uma substring existe em uma string 

print("maçã" not in frutas) # Confirmar se realmente a fruta não está na lista

print(200 in saques) # Confirmar se o valor 200 não está dentro dos valores de saque