import random


class Carta:

    def __init__(self,valor,color):
        self.Valor = valor
        self.Color = color
        
class Comodin(Carta):
    def __init__(self,valor,color):
        Carta.__init__(self,valor,color)
        self.Tipo = "Comodín"

class Numerica(Carta):
    def __init__(self,valor,color):
        Carta.__init__(self,valor,color)
        self.Tipo = "Numerica"
class Especial(Carta):
    def __init__(self,valor):
        Carta.__init__(self,valor,"Negro")
        self.Tipo = "Especial"

def crearMazoCartas():
    cartas = []
    colores = ["Rojo", "Azul", "Verde", "Amarillo"]
    especiales = ["Reverse", "Skip", "Draw 2"]
    # Cartas Normales
    for color in colores: 
        for numero in range(10):  
            carta = Numerica(numero,color)
            if numero == 0:
                cartas+= [carta]
            else:
                cartas += [carta]
                cartas += [carta] 
    #Especiales
    for color in colores:
        especial = 0
        for numero in range(3):
            carta = Comodin(color,especiales[especial])
            cartas+= [carta]
            cartas += [carta]
            especial += 1
    for color in range (4):
        carta = Especial("Wild")
        cartas += [carta]
    for color in range (4):
        carta = Especial("Wild Draw 4")
        cartas +=  [carta]

    #random.shuffle(cartas)

    for carta in cartas:
        print("Valor: "+str(carta.Valor))
        print("Color: "+carta.Color)
        print("Tipo: "+carta.Tipo)
    print(str(len(cartas)))


crearMazoCartas()

