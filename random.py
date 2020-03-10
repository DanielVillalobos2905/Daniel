from random import randint

lista = [randint(0, 100) for i in range(10)]

print (lista)

lista_ordenada = sorted(lista)
print(lista_ordenada)

lista_reversa = sorted(lista , reverse = True)
print(lista_reversa)
