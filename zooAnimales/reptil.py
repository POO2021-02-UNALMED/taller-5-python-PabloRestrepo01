from zooAnimales.animal import Animal
class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Animal._totalAnimales += 1
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Reptil._listado.append(self)
    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    
    @staticmethod
    def movimiento():
        return 'reptar'
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas += 1
        return Reptil(nombre, edad, 'humedal', genero, 'verdes', genero)
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.serpientes += 1
        return Reptil(nombre, edad, 'jungla', genero, 'blanco', 1)