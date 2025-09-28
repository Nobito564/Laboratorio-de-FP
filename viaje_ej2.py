distancia_km=384400
velocidad_kmh=5000
tiempo_horas=distancia_km//velocidad_kmh
tiempo_dias=tiempo_horas//24
print(f"tardarias {tiempo_dias}  dias en llegar.")

velocidad=float(input("introduce la velocidad en km/h:"))
tiempo=float(input('introduce el tiempo en horas:'))

distancia=velocidad*tiempo

print(f'el valor de la distancia es: {distancia}')

cadena_numero=distancia
entero=int(cadena_numero)
print(entero)
