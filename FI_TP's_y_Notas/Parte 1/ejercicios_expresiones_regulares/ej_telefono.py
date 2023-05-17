import re 

def find_tel(texto):
    return re.findall("(+54911)([0-9]{8})",texto)