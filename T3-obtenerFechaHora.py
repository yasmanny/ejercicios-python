# Ejercicio 3: Obtener la fecha y hora actuales en el sistema.

import datetime
#importar el modulo datetime, ofrece diversas funciones para trabajar con fecha y hora

ahora = datetime.datetime.now()
#obtener la fecha y hora actual mediante las funciones datetime.now()

print(ahora)

print(ahora.strftime('%d/%m/%y %H:%M:%S'))
#con la funcion .strftime() se puede configurar el como se mostrara la fecha y hora.