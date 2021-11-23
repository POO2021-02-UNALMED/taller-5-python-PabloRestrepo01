class Zona:
    def __init__(self, nombre, zoologico):
        self._nombre = nombre
        self._zoologico = zoologico
        self._animales = []
    
    def agregarAnimales(self, animal):
        self._animales.append(animal)
    
    def cantidadAnimales(self):
        return len(self._animales)