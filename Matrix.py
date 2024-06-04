import Array2D

class Matrix:
    def __init__(self, l, c):
        self.nRows = l
        self.nCols = c
        self.values = Array2D.Array2D(l, c)

    def print(self):
        self.values.print()

m = Matrix(4, 3)
m.print()
    