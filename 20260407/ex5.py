"""
Faça um algoritmo que calcule a área de um terreno.
 Os terrenos são retangulares, 
 e deverão ser informadas as medidas de 
 largura e comprimento do terreno.
"""
#entradas
largura = float(input("Informe a largura: "))
comprimento = float(input("Informe o comprimento: "))
#processamento
area = largura * comprimento
#saidas
print(f"A área do terreno é {area} m2")