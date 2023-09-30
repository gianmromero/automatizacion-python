#!Python 3.8
# Autor: https://n9.cl/3ej1z

import fitz

doc = fitz.open('sample.pdf')
# Cantidad de páginas en el pdf.
print(len(doc))
# Tomando página para su posterior procesamiento.
page = doc[0]

# Lista para guardar las co-ordenadas de todas las palabras subrayadas.
highlights = []
# Itera hasta hallar una anotación de subrayación en la página
annot = page.first_annot
while annot:
    if annot.type[0] == 8:
        all_coordinates = annot.vertices
        if len(all_coordinates) == 4:
            highlight_coord = fitz.Quad(all_coordinates).rect
            highlights.append(highlight_coord)
        else:
            all_coordinates = [all_coordinates[x:x+4] for x in
                            range(0, len(all_coordinates), 4)]
            for i in range(0, len(all_coordinates)):
                coord = fitz.Quad(all_coordinates[i]).rect
                highlights.append(coord)
        annot = annot.next 

all_words = page.get_text()

# Lista para guardar todas las palabras sobrayadas en el texto.
highlight_text = []

for h in highlights:
    sentence = [w[4] for w in all_words if fitz.Rect(w[0:4]).intersect(h)]
    highlight_text.append(" ".join(sentence))

print(" ".join(highlight_text))