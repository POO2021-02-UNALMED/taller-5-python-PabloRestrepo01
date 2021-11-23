from zooAnimales.animal import Animal
class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Animal._totalAnimales += 1
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Pez._listado.append(self)
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    
    @staticmethod
    def movimiento():
        return 'nadar'
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones += 1
        return Pez(nombre, edad, 'oceano', genero, 'rojo', 6)
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.bacalaos += 1
        return Pez(nombre, edad, 'oceano', genero, 'gris', 6)
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    
    def getColorEscamas(self):
        return self._colorEscamas

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas
    
    def getCantidadAletas(self):
        return self._cantidadAletas