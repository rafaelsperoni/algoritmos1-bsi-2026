"""
Faça um programa que receba o valor de um depósito
 e o valor da taxa de juros anual, 
 calcule e mostre o valor do rendimento 
 e o valor total depois do rendimento (após 1 ano);
"""
#ENTRADAS
deposito = float(input("Informe o valor: "))
taxa = float(input("Informe a taxa % anual: "))
#PROCESSAMENTO
rendimento = deposito * taxa / 100
total = deposito + rendimento
#SAIDAS
print(f"O rendimento após 12 meses foi de R${rendimento}")
print(f"O valor total é de R${total}")