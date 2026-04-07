"""
Faça um programa que receba o salário base de um funcionário, 
calcule e mostre o salário a receber, sabendo-se que o funcionário 
tem gratificação de 5% sobre o salário base e paga 7% de imposto 
também sobre o salário base;
"""

#ENTRADA
salario_base = float(input("Informe o salário base: "))
#PROCESSAMENTO
gratificacao = salario_base * 0.05
imposto = salario_base * 0.07
salario_receber = salario_base + gratificacao - imposto

#outra opção, usando apenas uma variável
#salario_receber = salario_base + salario_base * salario_base * 0.07
#SAIDA
print(f"O salário a receber: R${salario_receber}")

