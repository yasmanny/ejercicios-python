# Ejercicio 9: Mostrar la fecha de un evento almacenado en una tabla

fecha_evento = (2023, 9, 14)

#Primera forma mediante mapeo %
print('El evento programado sera para la fecha: %i/%i/%i' % fecha_evento)

#Segunda forma desempaquetar la tupla
anio, mes, dia = fecha_evento
print('El evento programado sera para ala fecha: {}/{}/{}'.format(anio, mes, dia))