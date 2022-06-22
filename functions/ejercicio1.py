base =int(input("Ingrese la base: "))
altura=int(input("Ingrese la altura: "))

def area(base,altura):
    return base*altura

areaTriangulo=area(base,altura)

print("El area del triangulo es: ",areaTriangulo)

radio=int(input("Ingrese el radio del circulo: "))

def areaCirculo(radio):
    return 3.14*radio**2

areaC=areaCirculo(radio)

print("El area del circulo es: ",areaC)