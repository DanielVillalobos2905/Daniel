# Realice un programa que lea por teclado 2 valores enteros positivos A y B, donde A > B. Debe asegurarse de que el A sea mayor que B. Luego:
# Cuente y muestre la cantidad de valores pares.
    
A = int(input('Ingrese un valor'))
B = int(input('Ingrese un valor'))
suma = 0 
if B < A:
    for c in range ( B, A+1):
        if c % 2 == 0:
            print (c)
            suma = suma + c
            print (suma )
            
     

       