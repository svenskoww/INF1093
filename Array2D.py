import Array1D

class Array2D:
    def __init__(self, nRows, nCols):
        self.nCols = nCols
        self.content = Array1D.Array1D(nRows)
        for i in range(nRows):
            self.content[i] = Array1D.Array1D(nCols)
            
    def numRows(self):
       return len(self.content)

    def numCols(self):
       return len(self.content[0])

    # Affiche le contenu du tableau
    def print(self):
        for i in range(self.numRows()):
                 print(self.content[i])

    # Initialisation du contenu du tableau a l'aide d'une valeur donnees
    def clear(self, value):
        for row in range(self.numRows()):
            self.content[row].clear(value)
            
    #
    def __setitem__(self, key, val):
        assert len(key)==2, "Nombre d'indices du tableau non valide."
        row = key[0]
        col = key[1]
        assert row >= 0 and row < self.numRows() and col >= 0 and col <= self.numCols() , "Nombre d'indices du tableau non valide."
        self.content[row][col] = val
    
    def __getitem__(self, key):
        assert len(key)==2, "Nombre d'indices du tableau non valide."
        row = key[0]
        col = key[1]
        assert row >= 0 and row < self.numRows() and col >= 0 and col <= self.numCols() , "Nombre d'indices du tableau non valide."
        line = self.content[row]
        return line[col]