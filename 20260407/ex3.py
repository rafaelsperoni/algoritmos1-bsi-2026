"""
Sabe-se que:
1 Pé = 12 polegadas
1 jarda = 3 pés
1 milha = 1.760 jardas
Faça um programa que receba uma medida em pés,
 faça as conversões e a seguir mostre os resultados em:
Polegadas
Jardas
Milhas
"""
#ENTRADAS
pes = float(input("Informe a medida em pés: "))
#PROCESSAMENTO
pol = pes * 12 #valor em polegadas
jar = pes / 3 #valor em jardas
mil = jar / 1760 #valor em milhas
#SAÍDAS
print(f"Equivale a {pol} polegadas")
print(f"Equivale a {jar} jardas")
print(f"Equivale a {mil} milhas")