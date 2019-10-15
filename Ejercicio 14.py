N = int(input('Ingrese un numero:'))
suma = 0
factorial = 1
if N>0: 
    for i in range (1, N +1):
        factorial *= i
        suma = suma + factorial
    print (suma)

else:
      print ('El numero no es valido')
      