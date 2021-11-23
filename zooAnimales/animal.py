from mamifero import Mamifero
from ave import Ave
from reptil import Reptil
from pez import Pez
from anfibio import Anfibio

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
        return 	"Mamiferos: " + Mamifero.cantidadMamiferos() +'''\n
		Aves: ''' +Ave.cantidadAves() + '''\n
		Reptiles: '''+Reptil.cantidadReptiles() +'''\n
		Peces: '''+Pez.cantidadPeces() +'''\n
		Anfibios: '''+Anfibio.cantidadAnfibios()
    
    def __str__(self):   
        retorno = 'Mi nombre es ' + self._nombre + ', tengo una edad de ' + self._edad + ', habito en ' +self._habitat + ' y mi genero es '+self._genero;
        
        if self._zona != None:
            retorno += ', la zona en la que me ubico es ' + self._zona +', en el ' + self._zona.getZoo()
        
        return retorno; 