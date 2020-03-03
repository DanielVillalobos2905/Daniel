N = int(input('ingrese un valor '))
lista = []
for i in range (N):
    valor = int(input('ingrese un valor')) 
    lista.append(valor)

suma = 0
for i in range (N):
    valor = lista[i]
    suma += valor
print (suma)    
