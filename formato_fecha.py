import re

#   Crear un Regex para el siguiente formato: 'DD/MM/YYYY'.
regex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
res = regex.search('Mi cumpleaños es: 08/11/1992')
#   TODO:Crear las condicionales para los rangos de días, meses y años.
if int(res.group(1)) >= 1 and int(res.group(1)) <= 31:
    if int(res.group(2)) >= 1 and int(res.group(2)) <= 12:
        if int(res.group(3)) >= 1000 and int(res.group(3)) <= 2999:
            print("Fecha validada")