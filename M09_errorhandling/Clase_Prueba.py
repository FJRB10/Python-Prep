class Pruebas():
    def __init__(self,lista):
        if (type(lista) == list):
            for i in lista:
                if type(i) != int:
                    raise TypeError("Solo se reciben listas con números enteros")
                else:
                    self.lista = lista
        else:
            raise TypeError("Solo se reciben listas con números enteros")

    def verificarPrimo(self):
        resultado = []

        for num in self.lista:
            primo = True
            i=num-1

            if num > 1:
                while i > 1:
                    if num%i == 0:
                        primo = False
                    i -= 1

                resultado.append(primo)
            else:
                resultado.append("El numero debe ser mayor que 1")
        
        for i in range(len(self.lista)):
            if resultado[i] == True:
                print("El número", self.lista[i], "si es primo")
            elif resultado[i] == False:
                print("El número", self.lista[i], "no es primo")
            else:
                print(resultado[i])
        
    def verificarPrimo2(self):
        resultado = []

        for num in self.lista:
            primo = True
            i=num-1

            if num > 1:
                while i > 1:
                    if num%i == 0:
                        primo = False
                    i -= 1

                resultado.append(primo)
            else:
                resultado.append(False)

        return(resultado)

    def valorModal(self):
        cont = 0
        rep = [0,0]

        self.lista.sort()

        while cont < len(self.lista):
            numero = self.lista[cont]
            repeticiones = self.lista.count(numero)
            cont += repeticiones

            if repeticiones > rep[1]:
                rep[0] = numero
                rep[1] = repeticiones
                cont = 0
            elif repeticiones == rep[1]:
                if numero != rep[0]:
                    rep.append(numero)
                    rep.append(repeticiones)

        if len(rep) > 2:
            pos = 0
            while pos < len(rep):
                print("El número", rep[pos], "se repitio", rep[pos+1], "veces")
                pos += 2
            
            return rep[:2]
        else:
            print("El número", rep[0], "se repitio", rep[1], "veces")
            
            return rep

    def conversionGrados(self,medidaOrigen,medidaDestino):
        for valor in self.lista:
            if medidaOrigen == "celcius" and medidaDestino == "farenheit":
                conversion = (valor * (9/5)) + 32
                print("La conversión de grados celcius a farenheit del valor", valor, "es igual a", conversion)
                #return conversion
            elif medidaOrigen == "celcius" and medidaDestino == "kelvin":
                conversion = valor + 273.15
                print("La conversión de grados celcius a kelvin del valor", valor, "es igual a", conversion)
                #return conversion
            elif medidaOrigen == "farenheit" and medidaDestino == "celcius":
                conversion = (valor - 32) * 5/9
                print("La conversión de grados farenheit a celcius del valor", valor, "es igual a", conversion)
                #return conversion
            elif medidaOrigen == "farenheit" and medidaDestino == "kelvin":
                conversion = (valor - 32) * (5/9) + 273.15
                print("La conversión de grados farenheit a kelvin del valor", valor, "es igual a", conversion)
                #return conversion
            elif medidaOrigen == "kelvin" and medidaDestino == "celcius":
                conversion = valor - 273.15
                print("La conversión de grados kelvin a celcius del valor", valor, "es igual a", conversion)
                #return conversion
            elif medidaOrigen == "kelvin" and medidaDestino == "farenheit":
                conversion = ((valor - 273.15) * 9/5) + 32
                print("La conversión de grados kelvin a farenheit del valor", valor, "es igual a", conversion)
                #return conversion
            else:
                raise ValueError("Alguna de las medidas esta mal escrita recuerde que es 'celcius', 'farenheit' y 'kelvin'.\nTodo en minuscula")
                #return "Alguna de las medidas esta mal escrita recuerde que es 'celcius', 'farenheit' y 'kelvin'.\nTodo en minuscula"

    def conversionGrados2(self,medidaOrigen,medidaDestino):
        resultado = []

        for valor in self.lista:
            if medidaOrigen == "celcius" and medidaDestino == "farenheit":
                conversion = (valor * (9/5)) + 32
                print("La conversión de grados celcius a farenheit del valor", valor, "es igual a", conversion)
                resultado.append(conversion)
            elif medidaOrigen == "celcius" and medidaDestino == "kelvin":
                conversion = valor + 273.15
                print("La conversión de grados celcius a kelvin del valor", valor, "es igual a", conversion)
                resultado.append(conversion)
            elif medidaOrigen == "farenheit" and medidaDestino == "celcius":
                conversion = (valor - 32) * 5/9
                print("La conversión de grados farenheit a celcius del valor", valor, "es igual a", conversion)
                resultado.append(conversion)
            elif medidaOrigen == "farenheit" and medidaDestino == "kelvin":
                conversion = (valor - 32) * (5/9) + 273.15
                print("La conversión de grados farenheit a kelvin del valor", valor, "es igual a", conversion)
                resultado.append(conversion)
            elif medidaOrigen == "kelvin" and medidaDestino == "celcius":
                conversion = valor - 273.15
                print("La conversión de grados kelvin a celcius del valor", valor, "es igual a", conversion)
                resultado.append(conversion)
            elif medidaOrigen == "kelvin" and medidaDestino == "farenheit":
                conversion = ((valor - 273.15) * 9/5) + 32
                print("La conversión de grados kelvin a farenheit del valor", valor, "es igual a", conversion)
                resultado.append(conversion)
            else:
                raise ValueError("Alguna de las medidas esta mal escrita recuerde que es 'celcius', 'farenheit' y 'kelvin'.\nTodo en minuscula")
                #return "Alguna de las medidas esta mal escrita recuerde que es 'celcius', 'farenheit' y 'kelvin'.\nTodo en minuscula"
            
        return resultado

    def factorial(self):
        listaResultado = []
        
        for num in self.lista:
            factor = self.factorial2(num)
            print("El factorial de", num, "es:", factor)
            listaResultado.append(factor)

        return listaResultado
            
    def factorial2(self,num):
        if num <= 0:
            return "El numero debe ser mayor a 0"
        elif type(num) != int:
            return "El numero debe ser entero"
        else:
            if num > 1:
                num = num * self.factorial2(num-1)
            return num