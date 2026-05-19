"""
Crie um algoritmo que leia um número, 
verifique e mostre se o número lido é par .
"""
#entradas
num = int(input("Informe um número inteiro: "))
resto = num % 2

if resto == 0:
    print(f"O número {num} informado é par")

print("Fim")