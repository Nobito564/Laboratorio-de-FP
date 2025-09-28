edad=int(input('introduce la edad de la persona:'))
nivel_fisico=int(input('introduce el nivel fisico:'))
while nivel_fisico < 1 or nivel_fisico > 10:
    print('ERROR: el valor debe estar entre 1 y 10')

    nivel_fisico=int(input('Introudce tu nivel fisico entre (1 y 10):'))

if edad >= 18 and nivel_fisico >=5:
 print("¡Listo para despegar!")
elif edad<18 and nivel_fisico<5:
   print('debes ser mayor de edad y estar en mejor forma')



