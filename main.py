#exercicio 1 - poligonos

'''lados = int(input("Diga o numero de lados: "))
if lados < 3:
    print("não é um poligono")
elif lados > 5:
    print("Poligono não identificado")
else:
    if lados == 3:
        forma = 'triangulo'
    elif lados == 4:
        forma = 'quadrado'
    else:
        forma = 'pentagono'
    medida = int(input("Qual a medida do lado?"))
    perimetro = lados*medida
    print(f"O poligono é um {forma} com perimetro de {perimetro}")'''

# exercicio 2 - verificar impar e par

#sem for e while 

n1 = int(input("1 | Digite um numero: "))
n2 = int(input("2 | Digite um numero: "))
n3 = int(input("3 | Digite um numero: "))
n4 = int(input("4 | Digite um numero: "))
n5 = int(input("5 | Digite um numero: "))
pares = 0
impares = 0
if n1%2 == 0:
    pares += 1
else:
    impares += 1
if n2%2 == 0:
    pares += 1
else:
    impares += 1
if n3%2 == 0:
    pares += 1
else:
    impares += 1
if n4%2 == 0:
    pares += 1
else:
    impares += 1
if n5%2 == 0:
    pares += 1
else:
    impares += 1
print(f"O numero de pares foi {pares} e o numero de impares foi {impares}")

# com for e while









    