#Contar la cantidad de números impares dentro de un intervalo cerrado de enteros [A,B].
A = int(input('ingrese un valor'))
B = int(input('ingrese un valor'))
suma = 0
for c in range (A , B+1):
    if c % 2 == 1:
        suma = suma + c
    
    print(suma)
