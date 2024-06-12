import Matrix as m
m1 = m.Matrix("matrice1.txt")

t1 = m1.trans()
tt1 = t1.trans()
m1.sub(tt1)
m1.print()

