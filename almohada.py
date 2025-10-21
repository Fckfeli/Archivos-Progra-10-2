# ------------------------------------------------------------
# Programa: Ejemplo práctico de la biblioteca Pillow
# Autor: Felipe
# Descripción:
#   Este programa crea una imagen nueva, dibuja un rectángulo
#   y escribe texto sobre ella usando la biblioteca Pillow.
#   Finalmente la guarda y la muestra al usuario.
# ------------------------------------------------------------

# Importamos los módulos necesarios de la biblioteca Pillow.
# Image: para crear y manipular imágenes.
# ImageDraw: para dibujar sobre las imágenes (líneas, formas, texto).
# ImageFont: para manejar fuentes de texto al escribir sobre la imagen.
from PIL import Image, ImageDraw, ImageFont

# Creamos una nueva imagen RGB (color) de 300 píxeles de ancho por 200 de alto.
# El color de fondo es azul cielo (RGB: 135, 206, 235).
imagen = Image.new("RGB", (300, 200), color=(135, 206, 235))

# Creamos un objeto 'dibujo' que nos permitirá dibujar sobre la imagen.
dibujo = ImageDraw.Draw(imagen)

# Dibujamos un rectángulo rojo (RGB: 255, 0, 0) con borde negro (RGB: 0, 0, 0).
# El rectángulo va desde la coordenada (50, 50) hasta (250, 150).
dibujo.rectangle([(50, 50), (250, 150)], fill=(255, 0, 0), outline=(0, 0, 0))

# Cargamos una fuente por defecto para escribir texto (no especificamos archivo de fuente).
fuente = ImageFont.load_default()

# Escribimos el texto "¡Hola desde Pillow!" sobre la imagen en la posición (85, 90).
# El color del texto es blanco (RGB: 255, 255, 255).
# Usamos la fuente cargada previamente.
dibujo.text((85, 90), "¡Hola desde Pillow!", fill=(255, 255, 255), font=fuente)

# Guardamos la imagen con el nombre 'resultado_pillow.png' en el disco.
imagen.save("resultado_pillow.png")

# Mostramos la imagen en el visor predeterminado del sistema operativo.
imagen.show()

# Imprimimos un mensaje en la consola para informar que todo se realizó correctamente.
print("Imagen creada y mostrada correctamente. Guardada como 'resultado_pillow.png'.")
