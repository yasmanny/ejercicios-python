# Ejercicio 2- exponer el uso de la funcion print.

print('Este es un ejemplo basico')

# con varios argumentos se mostraran como si fuera una sola frase
print('Python','es', 'tremendo')

# se puede colocar sepradadores entre los argumentos
print('Python', 'es', 'tremendo', sep='-')

# se pueden colocar placeholder {} que esta pendiente a llenar en la cadena de carcateres mediante la funcion .format()
print('{} es {}'.format('Python', 'tremendo'))

#tambien se puede usar para imprimir arreglos
numeros = [2, 4, 6, 8, 10]
print(numeros)

#tambien es capaz de imprimir diccionarios
capitales = {'Colombia': 'Bogota', 'Ecuador': 'Quito'}
print(capitales)