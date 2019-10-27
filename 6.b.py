A = int(input('Ingrese un valor'))
B = int(input('Ingrese un valor'))
suma = 0
if B < A:
    for c in range ( B , A+1 ):
        if c % 2 == 1:
               suma = c + suma
print (suma)     