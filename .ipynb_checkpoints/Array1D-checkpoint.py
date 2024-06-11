# Implemente la structure de donnees Tabelau 
import ctypes
class Array1D :
    # Creation d'un tableau avec size elements
    # Ce contructeur definit deux attributs : 
        # _size pour contenir le nombre d'element du tableau
        # _elements pour contenir la reference au tabelau
    def __init__(self, size):
        assert size > 0 , "La taille du tableau doit etre > 0"
        
        self._size = size   
        # Creation du tableau au moyen du module ctypes
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialise chaque element
        self.clear(0.0)
    # Retourne la taille du tableau
    def __len__(self):
        return self._size

    # Retourne l'element contenu a la position index
    def __getitem__(self, index):
        assert index>=0 and index<len(self), "Array subscript out of range"
        return self._elements[index]
    # Positionne la valeur dans le tableau a la position index
    def __setitem__(self, index, value):
        assert index>=0 and index<len(self), "Array subscript out of range"
        self._elements[index] = value
    # Reinitialise le tableau avec value a chaque position
    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    # Retourne un itterateur sur le tableau
    def __iter__(self):
        return _ArrayIterator(self._elements)
    # Affiche le tableau sur une ligne
    def __str__(self):
        # Retourne une représentation en chaîne formatée des décimaux
        return "[" + ", ".join(f"{d:.2f}" for d in self._elements) + "]"

# Un iterateur pour la structure de tabeleau
class _ArrayIterator :
    def __init__(self, theArray):
        self._arrayRef=theArray
        self._curNdx = 0
    def __iter__(self):
        return self
    def __next__(self):
        if(self._curNdx < len(self._arrayRef)):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration


