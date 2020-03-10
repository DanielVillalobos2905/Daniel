with open( 'miarchivo.txt' , 'w') as archivo:
    palabra = 'hola'
    archivo.write(palabra)
    valor = 123
    archivo.write(str(valor))

contenido = None
with open('miarchivo.txt' , 'r') as archivo:
    contenido = archivo.read()
print(contenido)
           