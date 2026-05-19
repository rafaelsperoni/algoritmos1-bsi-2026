#Criar um algoritmo que leia os limites inferior e superior de um intervalo e imprima 
# todos os números pares no intervalo aberto e seu somatório. 
#Suponha que os dados digitados são para um intervalo crescente, ou seja,  o primeiro valor é menor que o segundo. 
inferior = int(input("Informe o limite inferior: "))
superior = int(input("Informe o limite superior: "))

i = inferior+1
while i<superior:
    print(i)
    i+=1