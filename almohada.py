# ------------------------------------------------------------
# Programa: Ejemplo práctico de la biblioteca Pillow
# Autor: Felipe
# Descripción:
#   Este programa crea una imagen nueva, dibuja un rectángulo
#   y escribe texto sobre ella usando la biblioteca Pillow.
#   Finalmente la guarda y la muestra al usuario.
# ------------------------------------------------------------

from PIL import Image, ImageDraw, ImageFont

imagen = Image.new("RGB", (300, 200), color=(135, 206, 235))

dibujo = ImageDraw.Draw(imagen)

dibujo.rectangle([(50, 50), (250, 150)], fill=(255, 0, 0), outline=(0, 0, 0))

fuente = ImageFont.load_default()
dibujo.text((85, 90), "¡Hola desde Pillow!", fill=(255, 255, 255), font=fuente)

imagen.save("resultado_pillow.png")

imagen.show()

print("Imagen creada y mostrada correctamente. Guardada como 'resultado_pillow.png'.")
