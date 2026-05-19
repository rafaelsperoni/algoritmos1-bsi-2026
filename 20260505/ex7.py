#entradas
# receber codigo do cargo
while True:
    codigo = int(input("Informe o código do cargo: "))
    if codigo>0 and codigo<6:
        break
# receber salario atual
salario_atual = float(input("Informe o salário atual: "))

#processamento
# descobrir nome do cargo
# calcular o aumento
if codigo==1:
    nome_cargo = "Escriturário"
    percentual = 0.5
elif codigo == 2:
    nome_cargo = "Secretário"
    percentual = 0.35
elif codigo==3:
    nome_cargo = "Caixa"
    percentual = 0.2
elif codigo==4:
    nome_cargo = "Gerente"
    percentual = 0.1
else:
    nome_cargo = "Diretor"
    percentual = 0

aumento = salario_atual * percentual
novo_salario = salario_atual + aumento
#saidas
# mostrar nome do cargo
print(f"O nome do cargo é {nome_cargo}")
# mostrar o aumento
print(f"O aumento calculado é de {aumento}")
print(f"O novo salário é de {novo_salario}")