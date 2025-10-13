n = 1
def calculo(a,b,op):
    if op == 1:
        texto=(f'El resultado de la suma {a} + {b} es :{a + b} \n')
    elif op == 2:
        texto=(f'El resultado de la resta {a} - {b} es :{a - b} \n')
    elif op == 3:
        texto=(f'El resultado de la multiplicacion {a} * {b} es :{a * b} \n')
    else:
        texto=(f'El resultado de la division {a} / {b} es :{a / b} \n')
    
    return texto



while n < 5 and n > 0 :
    
    print('1. para sumar')
    print('2. para restar')
    print('3. multiplicar')
    print('4. dividir')
    print('Cualquier numero fuera del rango de indice del menu terminara la ejecucion de este programa.')
    
    
    n = int(input('selecciona su operacion: '))
    if n < 5 and n > 0:

        a = int(input('ingrese el primer valor: '))
        b = int(input('ingrese el segundo valor: '))
        print(calculo(a,b,n))
        n = 1
    else:
        break
print('programa finalizado.')

