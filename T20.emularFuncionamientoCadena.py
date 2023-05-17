#Ejercicio 20: Emular el funcionamiento del producto de cadenas

#python * 3 => pythonpythonpython

def prodcuto_cadena(cadena, repeticion):
    '''Emula el funcionamiento del producto (*) de cadena'''
    resultado = ''
    
    for i in range(repeticion):
        resultado += cadena
    
    return resultado

print('Python'*3)
print(prodcuto_cadena('python', 3))