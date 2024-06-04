{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e0694ddf-b4eb-4c3f-abdf-17a19b6548af",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Implemente la structure de donnees Tabelau \n",
    "import ctypes\n",
    "class Array :\n",
    "    # Creation d'un tableau avec size elements\n",
    "    # Ce contructeur definit deux attributs : \n",
    "        # _size pour contenir le nombre d'element du tableau\n",
    "        # _elements pour contenir la reference au tabelau\n",
    "    def __init__(self, size):\n",
    "        assert size > 0 , \"La taille du tableau doit etre > 0\"\n",
    "        \n",
    "        self._size = size   \n",
    "        # Creation du tableau au moyen du module ctypes\n",
    "        PyArrayType = ctypes.py_object * size\n",
    "        self._elements = PyArrayType()\n",
    "        # Initialise chaque element\n",
    "        self.clear(None)\n",
    "    # Retourne la taille du tableau\n",
    "    def __len__(self):\n",
    "        return self._size\n",
    "\n",
    "    # Retourne l'element contenu a la position index\n",
    "    def __getitem__(self, index):\n",
    "        assert index>=0 and index<len(self), \"Array subscript out of range\"\n",
    "        return self._elements[index]\n",
    "    # Positionne la valeur dans le tableau a la position index\n",
    "    def __setitem__(self, index, value):\n",
    "        assert index>=0 and index<len(self), \"Array subscript out of range\"\n",
    "        self._elements[index] = value\n",
    "    # Reinitialise le tableau avec value a chaque position\n",
    "    def clear(self, value):\n",
    "        for i in range(len(self)):\n",
    "            self._elements[i] = value\n",
    "\n",
    "    # Retourne un itterateur sur le tableau\n",
    "    def __iter__(self):\n",
    "        return _ArrayIterator(self._elements)\n",
    "    # Affiche le tableau sur une ligne\n",
    "    def __str__(self):\n",
    "        # Retourne une représentation en chaîne formatée des décimaux\n",
    "        return \"[\" + \", \".join(f\"{d:.2f}\" for d in self._elements) + \"]\"\n",
    "\n",
    "# Un iterateur pour la structure de tabeleau\n",
    "class _ArrayIterator :\n",
    "    def __init__(self, theArray):\n",
    "        self._arrayRef=theArray\n",
    "        self._curNdx = 0\n",
    "    def __iter__(self):\n",
    "        return self\n",
    "    def __next__(self):\n",
    "        if(self._curNdx < len(self._arrayRef)):\n",
    "            entry = self._arrayRef[self._curNdx]\n",
    "            self._curNdx += 1\n",
    "            return entry\n",
    "        else:\n",
    "            raise StopIteration\n",
    "\n",
    "\n",
    "\n",
    "            \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "6e8b7733-191e-475c-bd23-868ebf83f241",
   "metadata": {},
   "outputs": [],
   "source": [
    "import array\n",
    "\n",
    "class Array2D:\n",
    "    def __init__(self, nRows, nCols):\n",
    "        self.nCols = nCols\n",
    "        self.content = Array(nRows)\n",
    "        for i in range(nRows):\n",
    "            self.content[i] = Array(nCols)\n",
    "            \n",
    "    def numRows(self):\n",
    "       return len(self.content)\n",
    "\n",
    "    def numCols(self):\n",
    "       return len(self.content[0])\n",
    "\n",
    "     # Affiche le contenu du tableau\n",
    "    def print(self):\n",
    "        for i in range(self.numRows()):\n",
    "                 print(self.content[i])\n",
    "\n",
    "    # Initialisation du contenu du tableau a l'aide d'une valeur donnees\n",
    "    def clear(self, value):\n",
    "        for row in range(self.numRows()):\n",
    "            self.content[row].clear(value)\n",
    "            \n",
    "    #\n",
    "    def __setitem__(self, key, val):\n",
    "        assert len(key)==2, \"Nombre d'indices du tableau non valide.\"\n",
    "        row = key[0]\n",
    "        col = key[1]\n",
    "        assert row >= 0 and row < self.numRows() and col >= 0 and col <= self.numCols() , \"Nombre d'indices du tableau non valide.\"\n",
    "        self.content[row][col] = val\n",
    "        \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "dcb85cfb-41e4-418d-bb3e-cee666596bee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[42.00, 43.00, 14.00, 24.00]\n",
      "[20.00, 76.00, 23.00, 4.00]\n",
      "[50.00, 16.00, 24.00, 100.00]\n"
     ]
    }
   ],
   "source": [
    "filename = \"etudiants.txt\"\n",
    "# Ouvre le dichier en lecture\n",
    "gradeFile = open( filename, \"r\" )\n",
    "# Extraire les deux premières valeurs qui indiquent la taille du tableau.\n",
    "nExams = int( gradeFile.readline() )\n",
    "nStudents = int( gradeFile.readline() )\n",
    "# Créez le tableau 2D pour stocker les notes.\n",
    "examGrades = Array2D( nStudents, nExams )\n",
    "examGrades.clear(2.0)\n",
    "# Extraie les notes des lignes restantes.\n",
    "i = 0\n",
    "for student in gradeFile :\n",
    "    grades = student.split()\n",
    "    for j in range(nExams):\n",
    "        examGrades[i,j] = int(grades[j])\n",
    "    i+=1\n",
    "examGrades.print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "fcc86d62-5eb5-4b3c-8aa4-17cba978b34e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2.00, 2.00, 2.00, 2.00]\n",
      "[2.00, 2.00, 2.00, 2.00]\n",
      "[2.00, 2.00, 2.00, 2.00]\n"
     ]
    }
   ],
   "source": [
    "examGrades.print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fce307ad-ab82-4353-8df4-34e3cd20f1e1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
