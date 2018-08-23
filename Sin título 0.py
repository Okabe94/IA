import functions as ft
from nodoArbol import NodoArbol

estado_inicial = [[1,2,3],[4,8,6],[0,7,5]]
# [1,2,3]
# [4,8,6]
# [0,7,5]
           
solucion = [[1,2,3],[4,0,6],[7,8,5]]
# [1,2,3]
# [4,0,6]
# [7,8,5]
raiz = NodoArbol(estado_inicial)

loop = 1
found = False
while found:
    if(raiz.get_datos() == solucion):
        found = True
        print('Encontrado')
        break
    else:
        ft.move_all(solucion, raiz, loop)
    

def lower_cost(lis):
    if(not lis):
        return False
    for i in lis:
        
        