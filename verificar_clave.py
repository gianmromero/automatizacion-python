import re

#   Crear un Regex que verifique que la clave tenga al menos 8 caraceteres.
#   Crear un Regex que acepte mayúsculas y minúsculas.
#   Crear un Regex que permita tener dígitos.
regex = re.compile(r'(\w){8,}', re.IGNORECASE)
res = regex.search('abcD12ghIjk')

if res.group() != None:
    print("Contraseña validada")


