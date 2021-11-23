from zooAnimales.animal import Animal
class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Animal._totalAnimales += 1
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Anfibio._listado.append(self)
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    @staticmethod
    def movimiento():
        return 'saltar'
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        return Anfibio(nombre, edad, 'selva', genero, 'rojo', True)
        
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        return Anfibio(nombre, edad, 'selva', genero, 'rojo', True)