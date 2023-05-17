#Ejercicio 19: Comprobar si una cadena termina con la extension .py, sino en asi, agregar la extension

def validar_nombre(nombre_archivo):
    '''
    valida si un nombre de archivo tien la extension .py
    si el archivo no tiene la extension, lo arega
    '''
    if len(nombre_archivo) >= 3 and nombre_archivo[-3:] == '.py':
        return nombre_archivo
    
    return nombre_archivo + '.py'

print(validar_nombre('main.py'))
print(validar_nombre('modulo'))