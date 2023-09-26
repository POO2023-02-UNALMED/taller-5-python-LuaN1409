from zooAnimales.Animal import Animal

class Mamifero(Animal):
    caballos = 0
    leones = 0
    listado = []

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.listado.append(self)

    @staticmethod
    def cantidad_mamiferos():
        return len(Mamifero.listado)

    @staticmethod
    def crear_caballo(nombre, edad, genero):
        Mamifero.caballos += 1
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        Mamifero.listado.append(caballo)
        return caballo

    @staticmethod
    def crear_leon(nombre, edad, genero):
        Mamifero.leones += 1
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.listado.append(leon)
        return leon

    def is_pelaje(self):
        return self.pelaje

    def get_patas(self):
        return self.patas