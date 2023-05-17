#Ejercicio 7: Obtener la extension de un archivo espcificado por el usuario

#main.py => py
nombre_archivo = input('Ingrese el nombre del archivo: ')

partes_archivos = nombre_archivo.split('.')

print(partes_archivos)

print('La extension del archivo es {}'.format(partes_archivos[-1]))