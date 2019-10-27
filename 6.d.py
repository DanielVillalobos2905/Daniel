#crear programa que analice si el numero es primo o no
X = int(input("ingrese un numero "))
A = int(input('ingrese un valor de intervalor mayor a 1 '))
B = int(input('ingrese un valor de intervalo' ))
contador = 0
for n in range (A,B+1):
  if X % n == 0:
    contador = contador + 1
    print("divisor:", n)

if contador > 0 :
  print("El numero no es primo" )
else:
  print("El numero es primo")