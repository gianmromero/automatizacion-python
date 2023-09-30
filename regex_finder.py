#!python 3.8
# Según el input busca una palabra clave en un grupo de archivos y lo muestra.

from pathlib import Path
import pyinputplus as pyip

# Abrir todos los archivos de texto en la carpeta.
path = Path('D:/automatizacion-python/samples')

for nom in path.glob('*.txt'):
    p = Path(nom)
    content = p.read_text()
    print(content)

#   TODO: Buscar una palabra en los archivos de texto desde un input de usuario.
#   TODO: Mostrar los resultados en la pantalla.