
def myfuncion(name):
    print("Hello, " + name)

def suma(a,b):
    print(a+b)

myfuncion("Sergio")
suma(1,2)

#funciones anidadas

def maths(a,b):
    def suma():
        print(a+b)
    def resta():
        print(a-b)
    def multiplicacion():
        print(a*b)
    def division():
        print(a/b)
    suma()
    resta()
    multiplicacion()
    division()

def frase(**kwargs):
    if "coche" not in kwargs:
        return
    print("Hola, " + kwargs["nombre"] + " soy un " + kwargs["coche"])


frase(nombre="asd", coche="Ferrari")


#funciones lambda

anonymous = lambda x,y: x+y
print(anonymous(1,2))

