from zooAnimales.Animal import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0
    listado = []

    def __init__(self, nombre, edad, habitat, genero, color_escamas, cantidad_aletas):
        super().__init__(nombre, edad, habitat, genero)
        self.color_escamas = color_escamas
        self.cantidad_aletas = cantidad_aletas
        Pez.listado.append(self)

    @staticmethod
    def cantidad_peces():
        return len(Pez.listado)

    def movimiento(self):
        return "nadar"

    @staticmethod
    def crear_salmon(nombre, edad, genero):
        Pez.salmones += 1
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        Pez.listado.append(salmon)
        return salmon

    @staticmethod
    def crear_bacalao(nombre, edad, genero):
        Pez.bacalaos += 1
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.listado.append(bacalao)
        return bacalao

    def get_color_escamas(self):
        return self.color_escamas

    def get_cantidad_aletas(self):
        return self.cantidad_aletas