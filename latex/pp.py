import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Cadena a insertar al inicio
csnames = f"""
TWE




"""


# Abrir el archivo para leer
with open("pp.tex", "r", encoding="utf-8") as file:
    content = file.read()
##############################
# Buscar la posición de la cadena '%PORPROGRMALOANTERIOR'
marker = "%MIS_CSNAMES"

# Verificar si la cadena existe en el archivo
if marker in content:
    # Obtener el contenido desde la cadena '%PORPROGRMALOANTERIOR' hasta el final
    content_modified = content.split(marker, 1)[1]

    # Escribir el contenido modificado de nuevo en el archivo
    with open("pp.tex", "w", encoding="utf-8") as file:
        file.write(content_modified)
else:
    print(f"La cadena '{marker}' no se encontró en el archivo.")

##############################

csnames = csnames + "%MIS_CSNAMES\n"


# Abrir el archivo para leer
with open("pp.tex", "r", encoding="utf-8") as file:
    content = file.read()

# Insertar la cadena al inicio
content_modified = csnames + content

# Escribir el contenido modificado de nuevo en el archivo
with open("pp.tex", "w", encoding="utf-8") as file:
    file.write(content_modified)
