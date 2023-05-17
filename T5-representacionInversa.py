# Ejercicio 5: Obtener la representacion inversa de una cadena de caracteres

#Python => nohtyP
 
cadena = 'Python'

#mediante ciclo for
for i in range(len(cadena)-1, -1, -1):
    print(cadena[i], end="")

print()

#mediante rebanada
print(cadena[::-1])