from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
from gestion.zona import Zona

class Animal:
    totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = None
        Animal.totalAnimales += 1

    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def __str__(self):
        return f"Mamiferos: {Mamifero.cantidad_mamiferos()}\n" \
               f"Aves: {Ave.cantidad_aves()}\n" \
               f"Reptiles: {Reptil.cantidad_reptiles()}\n" \
               f"Peces: {Pez.cantidad_peces()}\n" \
               f"Anfibios: {Anfibio.cantidad_anfibios()}"

    def __str__(self):
        if self.zona is None:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}"
        else:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}, la zona en la que me ubico es {self.zona}, en el {self.zona.get_zoo().get_nombre()}"

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_habitat(self):
        return self.habitat

    def get_genero(self):
        return self.genero