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
            def creartxt():
                archi=open('Figura_triangulo.txt','w')
                archi.close
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            a = (base*altura)/ 2
            p = base * 3
            print("Area del triangulo =" ,a)
            print("Perimetro del triangulo: ",p)
            archi=open('Figura_triangulo.txt','a')
            archi.write('\nFigura triangulo:')
            archi.write('\nArea: '+str(a))
            archi.write('\nPerimetro: '+str(p))
            archi.close()
        
# cuadrilatero
        elif opcion == 4:
            def creartxt():
                archi=open('Figura_cuadrilatero.txt','w')
                archi.close
            lado = int(input("Ingrese la medida del lado: "))
            a = lado*lado
            p = lado * 4
            print("Area del cuadrado: ", lado * lado)
            print("Perimetro del cuadrado: ", 4 * lado)
            archi=open('Figura_cuadrilatero.txt','a')
            archi.write('\nFigura cuadrilatero:')
            archi.write('\nArea: '+str(a))
            archi.write('\nPerimetro: '+str(p))
            archi.close()


# pentagono
        elif opcion == 5:
            def creartxt():
                archi=open('Figura_pentagono.txt','w')
                archi.close
            lado = int(input("Ingrese la medida del lado: "))
            ap = int(input("Ingrese la medida del apotema: "))
            p = lado*5
            a = (p*ap)/2
            print("Area del pentagono: ",a)
            print("Perimetro del pentagono: ",p)
            archi=open('Figura_pentagono.txt','a')
            archi.write('\nFigura pentagono:')
            archi.write('\nArea: '+str(a))
            archi.write('\nPerimetro: '+str(p))
            archi.close()

# hexagono
        elif opcion == 6:
            def creartxt():
                archi=open('Figura_hexagono.txt','w')
                archi.close
            lado = int(input("Ingrese la medida del lado: "))
            ap = int(input("Ingrese la medida del apotema: "))
            p = lado*6
            a = (p*ap)/2
            print("Area del hexagono: ",a)
            print("Perimetro del hexagono: ",p)
            archi=open('Figura_hexagono.txt','a')
            archi.write('\nFigura hexagono:')
            archi.write('\nArea: '+str(a))
            archi.write('\nPerimetro: '+str(p))
            archi.close()

# heptagono
        elif opcion == 7:
            def creartxt():
                archi=open('Figura_heptagono.txt','w')
                archi.close
            lado = int(input("Ingrese la medida del lado: "))
            ap = int(input("Ingrese la medida del apotema: "))
            p = lado*7
            a = (p*ap)/2
            print("Area del heptagono: ",a)
            print("Perimetro del heptagono: ",p)
            archi=open('Figura_heptagono.txt','a')
            archi.write('\nFigura heptagono:')
            archi.write('\nArea: '+str(a))
            archi.write('\nPerimetro: '+str(p))
            archi.close()

# octagono
        elif opcion == 8:
            def creartxt():
                archi=open('Figura_octagono.txt','w')
                archi.close
            lado = int(input("Ingrese la medida del lado: "))
            ap = int(input("Ingrese la medida del apotema: "))
            p = lado*8
            a = (p*ap)/2
            print("Area del octagono: ",a)
            print("Perimetro del octagono: ",p)
            archi=open('Figura_octagono.txt','a')
            archi.write('\nFigura octagono:')
            archi.write('\nArea: '+str(a))
            archi.write('\nPerimetro: '+str(p))
            archi.close()
        
# eneagono
        elif opcion == 9:
            def creartxt():
                archi=open('Figura_eneagono.txt','w')
                archi.close
            lado = int(input("Ingrese la medida del lado: "))
            ap = int(input("Ingrese la medida del apotema: "))
            p = lado*9
            a = (p*ap)/2
            print("Area del eneagono: ",a)
            print("Perimetro del eneagono: ",p)
            archi=open('Figura_eneagono.txt','a')
            archi.write('\nFigura eneagono:')
            archi.write('\nArea: '+str(a))
            archi.write('\nPerimetro: '+str(p))
            archi.close()

# decagono
        elif opcion == 10:
            def creartxt():
                archi=open('Figura_decagono.txt','w')
                archi.close
            lado = int(input("Ingrese la medida del lado: "))
            ap = int(input("Ingrese la medida del apotema: "))
            p = lado*10
            a = (p*ap)/2
            print("Area del decagono: ",a)
            print("Perimetro del decagono: ",p)
            archi=open('Figura_decagono.txt','a')
            archi.write('\nFigura decagono:')
            archi.write('\nArea: '+str(a))
            archi.write('\nPerimetro: '+str(p))
            archi.close()
        
    print("")    
    opcion = int(input("Opciones:\nLados = 0 : No valido\nLados = 1 : No valido\nLados = 2 : No valido\nLados = 3 : triangulo\nLados = 4 : cuadrado\nLados = 5 : pentagono\nLados = 6 : hexagono\nLados = 7 : heptagono\nLados = 8 : octagono\nLados = 9 : eneagono\nLados = 10 : decagono\nIngrese el numero de lados: "))

  
