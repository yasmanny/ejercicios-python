#Ejercicio 16: Crear uan funcion para evaluar un numero y realizar una operacion

def diferencia(n):
    '''
    Calcula la diferencia del valor pasado como argumento.
    Sedeben seguir dos reglas
    '''
    if n <= 15:
        return 15 - n
    else:
        return(15-n)*2
    
print(diferencia(17))
print(diferencia(3))