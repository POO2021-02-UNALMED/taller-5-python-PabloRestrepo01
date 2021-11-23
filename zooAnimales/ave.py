from animal import Animal
class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0
    
    def __init__(self, colorPlumas, nombre, edad, habitat, genero):
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
        Animal._totalAnimales += 1
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None  
    
    @classmethod
    def cantidadAves(cls):
        len(cls._listado)
        
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
        return Ave(nombre, edad, 'montanas', 'blanco y amarillo')
        