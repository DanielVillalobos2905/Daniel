suma = 0
X = int(input('ingrese un valor'))
for i in range (1,X):
    if X % i == 0:
        suma += i
    
if suma == X:
    print ('es perfecto')
else:
    print ('el numero no es perfecto')

