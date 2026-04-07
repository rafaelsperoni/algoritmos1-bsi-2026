n1=7
n2=8
freq = 60
media = (n1+n2)/2
if freq<75:
    print("Reprovado por frequencia")
else: #senao
    if media>=7.0:
        print("Aprovado")
    else:
        print("Exame")

print("Tchau")