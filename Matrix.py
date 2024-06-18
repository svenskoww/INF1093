import Array2D as array2d

class Matrix:

    
    
    def __init__(self, filename=None,l=None, c=None,):
        if filename:
            with open(filename) as file:
                line = int(file.readline())
                col = int(file.readline())
                # Attribut de la classe
                self.nRows = line
                self.nCols = col
               
                self.values = array2d.Array2D(line, col)
                # Extract the values from the remaining lines.
                i = 0
                for line in file:
                    values = line.split()
                    for j in range(col):
                        self.values[i,j] = int(values[j])
                    i+=1
                file.close()
        else:
                self.nRows = l
                self.nCols = c
                self.values = array2d.Array2D(l, c)
            


    def get_nRows(self):
        return self.nRows
    
    def get_nCols(self):
        return self.nCols

    def print(self):
        self.values.print()
        
    def __getitem__(self,keys):
        row = keys[0]
        col = keys[1]
        assert row >= 0 and row < self.nRows and col >= 0 and col <= self.nCols , "Nombre d'indices du tableau non valide."
        return self.values[keys]

    def __setitem__(self,keys, val):
        row = keys[0]
        col = keys[1]
        assert row >= 0 and row < self.nRows and col >= 0 and col <= self.nCols , "Nombre d'indices du tableau non valide."
        self.values[keys]=val

   

    def add(self, m):
         assert (m.get_nRows() == self.nRows) and (m.get_nCols() == self.nCols) , "Les matrices sont incompatible pour une operation d'addition"
         for row in range(self.nRows):
             for col in range(self.nCols):
                 self[row, col] += m[row, col] 
    
    def sub(self, m):
         assert (m.get_nRows() == self.nRows) and (m.get_nRows() == self.nCols) , "Les matrices sont incompatible pour une operation de substraction"
         for row in range(self.nRows):
             for col in range(self.nCols):
                 self[row, col] -= m[row, col] 
    
    def scaleBy(self, f):
        for row in range(self.nRows):
             for col in range(self.nCols):
                 self[row, col] *= f
        
    
    def trans(self):
        t = Matrix(None,self.nCols, self.nRows)
        for col in range(t.nCols):
            for row in range(t.nRows):
                t[row, col] = self[ col, row]
        return t
    
    def mult(self, m):
        assert (m.get_nRows() == self.nCols)  , "Les matrices sont incompatible pour une operation de multiplication"
        prod = Matrix(None,self.nRows, m.get_nCols())
        for row in range(self.nRows):
            for col in range(m.get_nCols()):
                for k in range(self.nRows):
                    prod[row, col] += self[row, k]*m[k,row]
        return prod
    # Sous-matrice i j est la matrice prive des ligne i et j
    def under_matrice(self, i,j):
        assert (i>=0 and i <= self.nRows) and (j>=0 and j <= self.nCols) , "Les indices ne sont pas acceptables"
        under_m =  Matrix(None,self.nRows-1, self.get_nCols()-1)
        for row in range(self.nRows):
            for col in range(self.nCols):
                if(row < i and col < j):
                     under_m[row,col] = self[row,col]
                if(row > i and col > j):
                    under_m[row-1,col-1] = self[row,col]
                if(row > i and col < j):
                    under_m[row-1,col] = self[row,col]
                if(row < i and col > j):
                    under_m[row,col-1] = self[row,col]
        return under_m

    def determinant(self):
        assert (self.nRows == self.nCols)  , "La matrice doit etre carree"
        if(self.nRows == 2):
            return self[0, 0]*self[1,1] - self[1, 0]*self[0,1]
        if(self.nRows > 2):
             det = 0
             for i in range(self.nCols):
                 det += (self.under_matrice(0,i)).determinant()*((-1)**(i))*self[0,i]
             return det
        
    def inverse(self):
        assert self.determinant!=0 and self.nRows==self.nCols , "Cette matrice n'est pas inversible"
        t = self.trans()
        adjMat = Matrix( None, self.nRows,  self.nRows)
       
        for i in range( self.nRows):
            for j in range( self.nRows):
                adjMat[i,j] = (t.under_matrice(i,j)).determinant()*((-1)**(i+j))
       
        adjMat.scaleBy(self.determinant()**(-1))
        return adjMat





