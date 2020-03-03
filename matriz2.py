matriz = []

M = int(input('ingrese la cantidad de filas: '))
N = int(input('ingrese la cantidad de columnas: '))
t = 0

for i in range(M):
    matriz.append([])
    for j in range (N):
        valor = int(input('ingresa un valor: '))
        matriz[i].append(valor)
        
print(matriz)

suma = 0

for i in range(M):
   for j in range (N):
        valor = matriz[i][j]
        suma += valor
        
        
print(suma)