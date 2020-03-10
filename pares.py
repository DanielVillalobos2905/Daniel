from random import randint

lista = [randint(0, 10) for i in range(10)]
      
        
with open( 'pares.txt' , 'w') as archivo:
        for i in lista:
            if ( i % 2 == 0):
                archivo.write(str(i) + ' ')
            
            
        
    
with open('pares.txt' , 'r') as archivo:
    contenido = archivo.read()
print(lista)
print(contenido)
           

           