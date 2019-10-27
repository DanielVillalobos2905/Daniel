#Calcular y mostrar la sumatoria de los primeros N naturales.#
N = int(input('Ingrese un valor'))
suma = 0
for N in range ( 0 , N + 1):
    suma = suma + N
    print (suma) 
