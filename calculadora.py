def suma(a,b):
    resultado = a + b
    return resultado
a=int(input("ingrese el primer numero"))
b=int(input("ingrese el segundo numero"))
print(f"el resultado de la suma es {suma(a,b)}")

def resta(a,b):
    resultado = a - b
    return resultado
a=int(input("ingrese el primer numero"))
b=int(input("ingrese el segundo numero"))
print(f"el resultado de la resta es {resta(a,b)}")

def mutliplicacion(a,b):
    resultado = a * b
    return resultado
a=int(input("ingrese el primer numero"))
b=int(input("ingrese el segundo numero"))
print(f"el resultado de la multiplicaicon es {mutliplicacion(a,b)}")

def division(a,b):
    resultado = a / b
    return resultado
a=float(input("ingrese el primer numero"))
b=float(input("ingrese el segundo numero"))
print(f"el resultado de la division es {division(a,b)}")

def suma(a , b):
    resultado = a + b
    return resultado

def restar(a , b):
    resultado = a - b
    return resultado

def dividir(a , b):
    resultado = a / b
    return resultado

def multiplicar(a , b):
    resultado = a * b
    return resultado

print("""
escoja que operacion desea realizar
    1-suma
    2-resta
    3-multiplicar
    4-dividir
    5-salir

""")

resp = int(input("ingrese su opcion: "))

if resp == 1:
    num1 = int(input("ingrese el primer numero a sumar"))
    num2 = int(input("ingrese el segundo numero a sumar"))
    resultado = suma(num1, num2)
    print("El resultado de la suma es ", resultado)
elif resp == 2:
    num1 = int(input("ingrese el primer numero a restar"))
    num2 = int(input("ingrese el segundo numero a restar"))
    resultado = restar(num1, num2)
    print(resultado)
elif resp == 3:
    num1 = int(input("ingrese el primer numero a multiplicar"))
    num2 = int(input("ingrese el segundo numero a multiplicar"))
    resultado = multiplicar(num1, num2)
    print(resultado)
elif resp == 4:
    num1 = int(input("ingrese el primer numero a dividir"))
    num2 = int(input("ingrese el segundo numero a dividir"))
    resultado = dividir(num1, num2)
    print(resultado)
else:
    print("gracias ")
