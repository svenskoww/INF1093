# Retourne l 'indice du plus petit entre element a partir de l'indice begin a la fin 
def min_index(tab, begin):
    min = begin
    for i in range(begin,len(tab)):
        if(tab[i] < tab[min]):
            min = i
    return min

# permute les valeur des positionne dans le tableau aux indices donnees
def permut(i, j, tab):
     temp = tab[j]
     tab[j] = tab[i]
     tab[i] = temp
     
tab = [18, 4, 5, 3, 25, 0 , 14, -1 ]

# implementation du tri selection

def tri_selection(t):
    for i in range(len(t)):
        min = min_index(t, i)
        permut(i, min, t)
        print(t)
        
        
tri_selection(tab)
