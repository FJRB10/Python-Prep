from datetime import datetime

fecha = datetime.now()
temperatura = int(input("Digite el valor de temperatura. RECUERDE QUE ESTE VALOR DEBE SER EN GRADOS CENTIGRADOS(CELCIUS): "))
humedad = int(input("Digite el valor de la humedad: "))
lluvia = int(input("Digite 1 si llovio y 2 si no: "))

if lluvia < 1 or lluvia > 2:
    raise ValueError("El valor digitado debe ser 1 o 2 dependiendo si llovio o no, correspondientemente")
else:
    if lluvia == 1:
        lluvia2 = True
    elif lluvia == 2:
        lluvia2 = False

print("\n",
      "Temperatura:", temperatura, "\n",
      "Humedad:", humedad, "\n",
      "Lluvia:", lluvia2,"\n")

prueba4 = open('Clase10_ej2.csv', 'a')
prueba4.write(str(fecha) + ',')
prueba4.write(str(temperatura) + ',')
prueba4.write(str(humedad) + ',')
prueba4.write(str(lluvia2))
prueba4.write("\n")
prueba4.close()