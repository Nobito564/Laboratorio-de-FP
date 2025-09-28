import viaje_ej2

respuesta='s'
while respuesta == 's':
 distancia_km=int(input('introduzca la distancia en km/s: '))
 velocidad_kmh=int(input('introduzca la velocidad en km/h: '))

 tiempo_horas= distancia_km / velocidad_kmh
 tiempo_dias= tiempo_horas // 24
 print(f'tardaras {tiempo_dias} dias en llegar.')
 respuesta = input('¿quieres hacer otra simulacion? (s/n): ').lower

 cadena_numero=tiempo_dias
 entero=int(cadena_numero)
 print(entero)