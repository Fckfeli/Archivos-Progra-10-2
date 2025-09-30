# Se crea una lista de números enteros
lista_numeros = [1, 2, 3, 4, 5]

# Se crea una lista de cadenas (strings)
lista_strings = ['apple', 'banana', 'cherry']

# Se crea una lista con elementos de distintos tipos (mixta)
lista_mixta = [1, 'dos', True, 4.5]

# Se accede al primer elemento de la lista de números (índice 0)
primer_elemento = lista_numeros[0]

# Se accede al segundo elemento de la lista de strings (índice 1)
segundo_elemento = lista_strings[1]

# Se accede al último elemento de la lista mixta (índice -1)
ultimo_elemento = lista_mixta[-1]

# Se obtiene la longitud (cantidad de elementos) de la lista mixta
long = len(lista_mixta)
print(long)  # Imprime la longitud de la lista mixta

# Se agrega el número 6 al final de la lista de números
lista_numeros.append(6)

# Se inserta el string "orange" en la posición 1 de la lista de strings
lista_strings.insert(1, "orange")  # Ahora "orange" está entre "apple" y "banana"

# Se elimina y guarda el último elemento de la lista de números
ultimo_elemento = lista_numeros.pop()  # Elimina el 6 que se había añadido

# Se elimina el string "banana" de la lista de strings
lista_strings.remove("banana")  # Busca y elimina "banana" de la lista

# Se ordena la lista de números de menor a mayor
lista_numeros.sort()

# Se invierte el orden de los elementos en la lista mixta
lista_mixta.reverse()
