A = str(input('Ingrese un texto:'))
suma1 = 0
suma2 = 0
for c in A:
    if  c == 'a' or c == 'e' or c == 'i' or  c == 'o' or c == 'u':
        suma1 += 1
    else:
            suma2 += 1
        
print('El texto contiene', suma1, 'vocales')
print('El texto contiene', suma2, 'consonantes') 
        