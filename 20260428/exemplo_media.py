n1 = float(input("Informe n1: "))
n2 = float(input("Informe n1: "))
freq = float(input("Informe o percentual de frequência: "))

media = (n1 + n2) / 2

print(f"A média: {media}")

if freq>=75:
    if media>=7.0:
        print("Aprovado por média.")
    else:
        exame = float(input("Informe nota do exame: "))
        media = (media + exame) / 2

        if media>=5.0:
            print("Aprovado no exame.")
        else:
            print("Reprovado.")
            print("Reprovado.")
else:
    print("Reprovado por frequencia!")

#verificar o conceito equivalente
if media>=0 and media<2:
    conceito = "E"
elif media<4:
    conceito = "D"
elif media < 6:
    conceito = "C"
elif media < 8:
    conceito = "B"
else:
    conceito = "A"
############ sem else - ifs independentes ##################################

if media>=0 and media < 2:
    conceito = "E"
if media>=2 and media < 4:
    conceito = "D"
if media>=4 and media < 6:
    conceito = "C"
if media>=6 and media < 8:
    conceito = "B"
if media>=8 and media < 10:
    conceito = "A"
