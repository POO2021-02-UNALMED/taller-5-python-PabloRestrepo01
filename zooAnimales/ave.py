from zooAnimales.animal import Animal
class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        self._colorPlumas = colorPlumas
        Animal._totalAnimales += 1
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None 
        Ave._listado.append(self)
    
    @classmethod
    def cantidadAves(cls):
        str(len(cls._listado))
        
    @staticmethod
    def movimiento():
        return 'volar'
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return Ave(nombre, edad, 'montanas', genero, 'cafe glorioso')
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return Ave(nombre, edad, 'montanas', genero, 'blanco y amarillo')

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas