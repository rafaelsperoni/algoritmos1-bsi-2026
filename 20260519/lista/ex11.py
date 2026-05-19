#11 - Escreva um algoritmo que receba 15 números e imprima quantos números maiores que 30 foram digitados. 

i = 0
maiores = 0
while i<15:
    num = int(input("Informe o numero: "))
    if num>30:
        maiores += 1
    i+=1

print(f"Quantidade de valores maiores que 30: {maiores}")