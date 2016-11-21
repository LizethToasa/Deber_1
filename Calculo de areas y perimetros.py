# FIGURAS GEOMETRICAS
# Fecha: 21-Nov-2016

pi = 3.1416
print("****CALCULO DE AREAS Y PERIMETRO****")
print("Nombres:Padilla Geovanny\n\tSaldaña David\n\tToasa Lizeth")
print("\n")
print("1=circulo\n2=triangulo\n3=rectangulo\n4=cuadrado\notro=stop ")
print("")
opcion = int(input("Ingrese la figura:\n1=circulo\n2=triangulo\n3=rectangulo\n4=cuadrado\notro=stop: "))
while opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:

# circulo
    if opcion == 1:
        diametro = float(input("Ingrese diametro:"))
        radio = diametro / 2
        print("Area del circulo =" , radio * radio * pi)
        print("Perimetro del circulo: ", 2 * pi * radio)
        

# triangulo
    elif opcion == 2:
        base = float(input("base: "))
        altura = float(input("altura: "))
        print("Area del triangulo =", base * altura / 2)

# rectangulo
    elif opcion == 3:
        base = float(input("base: "))
        altura = float(input("altura: "))
        print("Area del rectangulo =", base * altura)
        print("Perimetro del rectangulo: ", 2*base + 2*altura)

# cuadrado
    elif opcion == 4:
        lado = int(input("Ingrese el lado: "))
        print("Area del cuadrado: ", lado ** 2)
        print("Perimetro del cuadrado: ", 4 * lado)
        
    print("")    
    opcion = int(input("Ingrese la figura:\n1=circulo\n2=triangulo\n3=rectangulo\n4=cuadrado\notro=stop: "))
