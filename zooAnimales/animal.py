

class Animal:
    _totalAnimales = 0
    
    def __init__(self, nombre, edad, habitat, genero):
        Animal._totalAnimales += 1
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
    
    @staticmethod
    def movimiento():
        return 'desplazarse'
    
    def totalPorTipo():
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio
        return 	"Mamiferos: " + str(Mamifero.cantidadMamiferos()) +'''
		Aves: ''' +str(Ave.cantidadAves()) + '''
		Reptiles: '''+str(Reptil.cantidadReptiles()) +'''
		Peces: '''+str(Pez.cantidadPeces()) +'''
		Anfibios: '''+str(Anfibio.cantidadAnfibios())
    
    def toString(self):   
        retorno = 'Mi nombre es ' + self._nombre + ', tengo una edad de ' + str(self._edad) + ', habito en ' +self._habitat + ' y mi genero es '+self._genero;
        
        if self._zona != None:
            retorno += ', la zona en la que me ubico es ' + self._zona +', en el ' + self._zona.getZoo()
        
        return retorno
    
    def setNombre(self, nombre):
            self._nombre = nombre
        
    def getNombre(self):
        return self._nombre
    
    def setEdad(self, edad):
            self._edad = edad
        
    def getEdad(self):
        return self._edad
    
    def setHabitat(self, habitat):
        self._habitat = habitat
        
    def getHabitat(self):
        return self._habitat

    def setGenero(self, genero):
        self._genero = genero
        
    def getGenero(self):
        return self._genero