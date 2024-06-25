tab = [8, 4, 5, 3, 25, 0 , 14, -1]

def permut(t,i, j):
     temp = t[j]
     t[j] = t[i]
     t[i] = temp
     
def tri_bulle(tab):
   
    while(True):
        permutation = 0
        print(tab)
        for i in range(len(tab)):
            if(i <len(tab)-1):
                if tab[i]>tab[i+1]:
                    permut(tab,i, i+1)
                    permutation+=1
        print(permutation)         
        if(permutation==0):
             break

tri_bulle(tab)

