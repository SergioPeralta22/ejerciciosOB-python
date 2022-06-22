def numeroprimo():
    numero: int = int(input("Introduce un numero entero: "))

    if numero > 1:
        for i in range(2, int(numero)):
            if (int(numero) % i) == 0:
                print(f"El numero {numero} no es primo, es divisible entre {i}")
                break
            else:
                print(f"El numero {numero} es primo!")
    else:
        print(f"El numero {numero} no es primo porque debe ser mayor que 1")
        