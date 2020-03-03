lista = [1,3.4,True , 'hola']
N = 4
for i in range (N):
    valor = i
    lista.append(valor)
print(lista)

lista = [i for i in range(N)]
print(lista)

lista1 = [1,2,4]
lista2 = [3,5,2]
for a , b in zip (lista1 , lista2):
    print(a,b)