from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    listado = []

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, color_piel=None, venenoso=None):
        super().__init__(nombre, edad, habitat, genero)
        self.color_piel = color_piel
        self.venenoso = venenoso
        Anfibio.listado.append(self)

    @staticmethod
    def cantidad_anfibios():
        return len(Anfibio.listado)

    def movimiento(self):
        return "saltar"

    @staticmethod
    def crear_rana(nombre, edad, genero):
        Anfibio.ranas += 1
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio.listado.append(rana)
        return rana

    @staticmethod
    def crear_salamandra(nombre, edad, genero):
        Anfibio.salamandras += 1
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        Anfibio.listado.append(salamandra)
        return salamandra

    def get_color_piel(self):
        return self.color_piel

    def is_venenoso(self):
        return self.venenoso