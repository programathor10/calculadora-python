def suma(a,b):
    return a + b
    

def resta(a,b):
    return a - b
     

def multiplicacion(a,b):
    return a * b
    

def division(a,b):    
    return a / b
    


def menu():
    print("1. para sumar")
    print("2. para restar")
    print("3. multiplicar")
    print("4. dividir")
    print("0. Cerrar aplicacion")

    n = int(input("selecciona su operacion: "))

    return n


def calcular(n):
    
    try:
        a = float(input("ingrese el primer valor: "))
        b = float(input("ingrese el segundo valor: "))
        
        if n == 1:
            resultado = suma(a,b)
        elif n == 2:
            resultado = resta(a,b)
        elif n == 3:
            resultado = multiplicacion(a,b)
        elif n == 4:
            try:
                resultado = division(a,b)
            except ZeroDivisionError:
                resultado = "El divisor no puede ser 0"
        
        return resultado
    
    except ValueError:
        resultado = "Solo se opera con valores numericos."
        return resultado



def main():

    n=-1

    while n !=0:
        try:
            n=menu()
            if n == 0:
                break  
        except ValueError:
            print("ingrese un valor numerico.")
            continue
        
        if n not in range(0, 5):
            print("Ingresá un número entre 0 y 4")
            continue
        resultado = calcular(n)
        print(resultado)


main()