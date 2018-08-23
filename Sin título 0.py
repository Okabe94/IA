import functions as ft
from nodoArbol import NodoArbol

def lower_cost(root):
    lis = root.get_hijo()
    if(not lis):
        return False
    cost = lis[0].get_coste()
    nodo = lis[0]
    for i in lis:
        if(i.get_coste() < cost):
            cost = i.get_coste()
            nodo = i
    return nodo

estado_inicial = [[3,2,1],[0,5,6],[4,7,8]]
# [3,2,1]
# [0,5,6]
# [4,7,8]
           
solucion = [[1,2,3],[4,0,6],[7,8,5]]
# [1,2,3]
# [4,0,6]
# [7,8,5]

root = NodoArbol(estado_inicial)
loop = 1
found = True
visited = []
while found:
    if(root.get_datos() == solucion):
        found = False
        print('Solution found')
        break
    else:
        ft.move_all(solucion, root, loop, visited)
        root = lower_cost(root)
        print(str(loop))
        loop+=1
        
    

        
        