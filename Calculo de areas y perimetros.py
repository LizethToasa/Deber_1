# FIGURAS GEOMETRICAS
# Fecha: 21-Nov-2016
print("****CALCULO DE AREAS Y PERIMETRO****")
print("Nombres:Padilla Geovanny\n\tSaldaña David\n\tToasa Lizeth")
print("\n")

opcion = int(input("Opciones:\nLados = 0 : No valido\nLados = 1 : No valido\nLados = 2 : No valido\nLados = 3 : triangulo\nLados = 4 : cuadrado\nLados = 5 : pentagono\nLados = 6 : hexagono\nLados = 7 : heptagono\nLados = 8 : octagono\nLados = 9 : eneagono\nLados = 10 : decagono\nIngrese el numero de lados: "))
while opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5 or opcion == 6 or opcion == 7 or opcion == 8 or opcion == 9 or opcion == 10 or opcion == 0:
    if (opcion == 1 or opcion == 2 or opcion == 0):
      print("No se puede realizar el calculo del perimetro y el area debido a que el numero de lados = ",opcion,"no forma una figura geometrica")
    else:

# triangulo
        if opcion == 3:
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            a = (base*altura)/ 2
            p = base * 3
            print("Area del triangulo =" ,a)
            print("Perimetro del triangulo: ",p)
        
# cuadrilatero
        elif opcion == 4:
            lado = int(input("Ingrese la medida del lado: "))
            print("Area del cuadrado: ", lado * lado)
            print("Perimetro del cuadrado: ", 4 * lado)


# pentagono
        elif opcion == 5:
            lado = int(input("Ingrese la medida del lado: "))
            ap = int(input("Ingrese la medida del apotema: "))
            p = lado*5
            a = (p*ap)/2
            print("Area del pentagono: ",a)
            print("Perimetro del pentagono: ",p)

# hexagono
        elif opcion == 6:
            lado = int(input("Ingrese la medida del lado: "))
            ap = int(input("Ingrese la medida del apotema: "))
            p = lado*6
            a = (p*ap)/2
            print("Area del hexagono: ",a)
            print("Perimetro del hexagono: ",p)

# heptagono
        elif opcion == 7:
            lado = int(input("Ingrese la medida del lado: "))
            ap = int(input("Ingrese la medida del apotema: "))
            p = lado*7
            a = (p*ap)/2
            print("Area del heptagono: ",a)
            print("Perimetro del heptagono: ",p)

# octagono
        elif opcion == 8:
            lado = int(input("Ingrese la medida del lado: "))
            ap = int(input("Ingrese la medida del apotema: "))
            p = lado*8
            a = (p*ap)/2
            print("Area del octagono: ",a)
            print("Perimetro del octagono: ",p)
        
# eneagono
        elif opcion == 9:
            lado = int(input("Ingrese la medida del lado: "))
            ap = int(input("Ingrese la medida del apotema: "))
            p = lado*9
            a = (p*ap)/2
            print("Area del eneagono: ",a)
            print("Perimetro del eneagono: ",p)

# decagono
        elif opcion == 10:
            lado = int(input("Ingrese la medida del lado: "))
            ap = int(input("Ingrese la medida del apotema: "))
            p = lado*10
            a = (p*ap)/2
            print("Area del decagono: ",a)
            print("Perimetro del decagono: ",p)
        
    print("")    
    opcion = int(input("Opciones:\nLados = 0 : No valido\nLados = 1 : No valido\nLados = 2 : No valido\nLados = 3 : triangulo\nLados = 4 : cuadrado\nLados = 5 : pentagono\nLados = 6 : hexagono\nLados = 7 : heptagono\nLados = 8 : octagono\nLados = 9 : eneagono\nLados = 10 : decagono\nIngrese el numero de lados: "))

  
