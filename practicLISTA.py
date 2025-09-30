frutlista=["piña","papaya","melon","fresas"]
print(frutlista)
elemento0=frutlista[0]
print (elemento0)
frutlista.append("kiwi")
print(frutlista)
frutlista.insert(1,"pera")
print(frutlista)
frutlista.remove("kiwi")
print(frutlista)

coordenadas = (3, 7)

# Acceso a elementos
x = coordenadas[0]  # x es igual a 3

# Longitud de la tupla
longitud = len(coordenadas)  # longitud es igual a 2

# Desempaquetado de tuplas
a, b = coordenadas  # a es igual a 3, b es igual a 7

# Concatenación de tuplas
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
tupla_concatenada = tupla1 + tupla2  # tupla_concatenada es igual a (1, 2, 3, 'a', 'b', 'c')

# Creación de un objeto range
mi_rango = range(0, 10, 2)

# Iteración sobre el rango
for numero in mi_rango:
    print(numero)  # Imprime 0, 2, 4, 6, 8

# Convertir el rango en una lista
lista_mi_rango = list(mi_rango)  # lista_mi_rango es igual a [0, 2, 4, 6, 8]

# Verificar si un valor está en el rango
esta_en_rango = 3 in mi_rango  # devuelve False