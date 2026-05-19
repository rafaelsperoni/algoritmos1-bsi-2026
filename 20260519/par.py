#repetir 10 vezes
i = 0
pares = 0
impares = 0
while pares < 3:
    num = int(input("Informe um numero: "))
    if num%2 == 0:
       print("par")
       pares += 1
    else:
       print("impar")
       impares +=1
    #incremento do contador
    i += 1 # i = i + 1

print(f"Você informou {i} valores")
print(f"{pares} são pares")
print(f"{impares} são impares")