distancia_marte = 225000000
for velocidad in range(10000, 50001, 10000):
    tiempo_en_horas = distancia_marte / velocidad
    tiempo_en_dias = tiempo_en_horas / 24
    print(f"Velocidad: {velocidad} km/h -> Tiempo: {tiempo_en_dias} días")
