#crear programa que analice si el numero es primo o no
X = int(input("ingrese un numero "))
contador = 0
for n in range (2, X):
  if X % n == 0:
    contador = contador + 1
    print("divisor:", n)

if contador > 0 :
  print("El numero no es primo" )
else:
  print("El numero es primo")
     
            