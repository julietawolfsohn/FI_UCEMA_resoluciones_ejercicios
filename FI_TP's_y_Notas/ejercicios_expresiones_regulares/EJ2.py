#Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.
def caracteres_permitidos(string):
    return not bool(re.search('[^a-zA-Z0-9]',string))

# No me puede dar True si por ejemplo pongo b