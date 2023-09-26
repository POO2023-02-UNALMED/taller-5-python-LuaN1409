from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0
    listado = []

    def __init__(self, nombre, edad, habitat, genero, color_escamas, largo_cola):
        super().__init__(nombre, edad, habitat, genero)
        self.color_escamas = color_escamas
        self.largo_cola = largo_cola
        Reptil.listado.append(self)

    @staticmethod
    def cantidad_reptiles():
        return len(Reptil.listado)

    def movimiento(self):
        return "reptar"

    @staticmethod
    def crear_iguana(nombre, edad, genero):
        Reptil.iguanas += 1
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        Reptil.listado.append(iguana)
        return iguana

    @staticmethod
    def crear_serpiente(nombre, edad, genero):
        Reptil.serpientes += 1
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil.listado.append(serpiente)
        return serpiente

    def get_color_escamas(self):
        return self.color_escamas

    def get_largo_cola(self):
        return self.largo_cola