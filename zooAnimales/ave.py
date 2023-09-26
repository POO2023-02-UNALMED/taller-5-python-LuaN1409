from zooAnimales.Animal import Animal

class Ave(Animal):
    plural = "Aves"
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, color_plumas):
        super().__init__(nombre, edad, habitat, genero)
        self.color_plumas = color_plumas
        Ave.listado.append(self)

    @staticmethod
    def cantidad_aves():
        return len(Ave.listado)

    def movimiento(self):
        return "volar"

    @staticmethod
    def get_listado():
        return Ave.listado

    @staticmethod
    def set_listado(listado):
        Ave.listado = listado

    def get_color_plumas(self):
        return self.color_plumas

    def set_color_plumas(self, color_plumas):
        self.color_plumas = color_plumas

    @staticmethod
    def crear_halcon(nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @staticmethod
    def crear_aguila(nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")