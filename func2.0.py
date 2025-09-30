#def nombre_de_la_funcion(parametro1, parametro2):
    #codigo de la funcion
def saludar(nombre):
    mensaje= f"hola, {nombre}"
    print(mensaje)
saludar("pepito")

def suma(a,b):
    resultado = a + b
    return resultado

resultado = suma(5,5)
print(resultado)

def area_rectangulo(base, altura):
    area = base * altura
    return area

base= int(input("ingrese el valor de la base del rectangulo"))
altura=int(input("ingrese el valor de la altura del rectangulo"))
area = area_rectangulo(base, altura)
print(area)

print(dir(__builtins__))
help(print)
print("hola", "mundo", sep="*")