#12 - Escreva um algoritmo que leia 20 números e imprima a soma dos positivos e o total de números negativos. 

i = 0
somapositivos = 0
negativos = 0
while i<20:
    num = int(input("Informe o numero: "))
    if num>0:
       somapositivos += num
    elif num<0:
        negativos += 1
    i+=1

print(f"Soma dos positivos: {somapositivos}")
print(f"Quantidade de negativos: {negativos}")