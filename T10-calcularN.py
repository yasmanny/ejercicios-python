#Ejercicio 10: Solicitar al usuario n y calcular n + nn + nnn

n = input('Escriba el valor de n: ')

n = int(n)
#covertimos en numero la cadena de n que se necesita
nn = int('{}{}'.format(n,n))
nnn = int('%s%s%s' % (n,n,n))

suma = n + nn + nnn

print(suma)