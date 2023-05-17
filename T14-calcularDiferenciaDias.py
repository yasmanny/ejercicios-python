#Ejercicio 14: calcular la diferencia en dias de dos fechas dadas.

from datetime import date

hoy=date(2023, 5, 17)
otra_fecha = date(2023, 9, 30)

delta = otra_fecha - hoy

print(delta)
print(delta.days)