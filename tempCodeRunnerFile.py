lados = int(input("Diga o numero de lados: "))
medida = int(input("Qual é a medida do ladp?"))
if lados < 3:
    print("não é um poligono")
elif lados == 3:
    forma = 'triangulo'
    perimetro = lados*medida
elif lados == 4:
    forma = 'quadrado'
    perimetro = lados*medida
elif lados == 5:
    forma = 'pentagono'
    perimetro = lados*medida
else:
    print("Poligono não identificado")