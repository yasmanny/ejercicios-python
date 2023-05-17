#ejercicio 6: Obtener un conjunto de numeros separados por coma y crear una lista

entrada = input('Escriba varios numeros separados por coma: ')

print(entrada)
print(type(entrada))
#comos e observa la entreda se presenta como una cadena de caracteres y no como una lista 

#para hacerlos lista usamos el metodo .split() indicando un separador  ','
numeros = entrada.split(',')
print(type(numeros))
print(numeros)