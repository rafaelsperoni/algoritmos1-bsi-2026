"""
 Faça um programa que leia três valores inteiros
 fornecidos pelo usuário e 
 exiba o maior e o menor dos valores lidos. 
 Supor que não sejam iguais.
"""
#entradas
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
#processamento
if a>b and a>c:
    maior = a

if b>a and b>c:
    maior = b

if c>a and c>b:
    maior = c

if a<b and a<c:
    menor = a

if b<a and b<c:
    menor = b

if c<a and c<b:
    menor = c
#saidas
print(f"O maior é {maior}")
print(f"O menor é {menor}")
