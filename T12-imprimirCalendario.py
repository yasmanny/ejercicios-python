#Ejercicio 12: Imprimir el calendario para un anio y mes especifico

import calendar
#el modulo calendar tiene el metodo .month que trabaja con un anio y mes para obtener un calendario

anio = int(input('Escriba el anio: '))
mes = int(input('Escriba el mes: '))

print(calendar.month(anio,mes))