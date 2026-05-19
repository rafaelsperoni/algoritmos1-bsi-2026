#8 - Criar um algoritmo que leia dez números inteiros e imprima o maior e o menor número. 
i = 0

while i<10:
    num = int(input(f"Informe o {i+1}o número: "))

    if i==0:
        maior = num
        menor = num
    else:
        if num>maior:
            maior = num
        elif num<menor:
            menor = num
    i+=1

print(f"O maior é {maior}")
print(f"O menor é {menor}")