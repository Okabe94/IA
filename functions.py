from copy import deepcopy
from nodoArbol import NodoArbol

def move_up(mat):
    newMat = deepcopy(mat)
    tup = look_up(newMat)
    if(tup[0]==0):
        return False
    else:
        aux = newMat[tup[0]-1][tup[1]]
        newMat[tup[0]-1][tup[1]] = newMat[tup[0]][tup[1]]
        newMat[tup[0]][tup[1]] = aux
        return newMat
    
def move_down(mat):
    newMat = deepcopy(mat)
    tup = look_up(newMat)
    if(tup[0]==(len(mat)-1)):
        return False
    else:
        aux = newMat[tup[0]+1][tup[1]]
        newMat[tup[0]+1][tup[1]] = newMat[tup[0]][tup[1]]
        newMat[tup[0]][tup[1]] = aux
        return newMat
    
def move_left(mat):
    newMat = deepcopy(mat)
    tup = look_up(newMat)
    if(tup[1]==0):
        return False
    else:
        aux = newMat[tup[0]][tup[1]-1]
        newMat[tup[0]][tup[1]-1] = newMat[tup[0]][tup[1]]
        newMat[tup[0]][tup[1]] = aux
        return newMat

def move_right(mat):
    newMat = deepcopy(mat)
    tup = look_up(newMat)
    if(tup[1]==(len(mat[tup[1]])-1)):
        return False
    else:
        aux = newMat[tup[0]][tup[1]+1]
        newMat[tup[0]][tup[1]+1] = newMat[tup[0]][tup[1]]
        newMat[tup[0]][tup[1]] = aux
        return newMat
    
def look_up(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if(mat[i][j]==0):
                return (i,j)
            
def move_all(sol, nodo, loop):
    mat = move_up(nodo.get_datos())
    if(mat):
        hijo = NodoArbol(mat)
        hijo.set_coste(find_cost(sol,hijo.get_datos())+loop)
        nodo.set_hijo(hijo)
    mat = move_down(nodo.get_datos())
    if(mat):
        hijo = NodoArbol(mat)
        hijo.set_coste(find_cost(sol,hijo.get_datos())+loop)
        nodo.set_hijo(hijo)
    mat = move_left(nodo.get_datos())
    if(mat):
        hijo = NodoArbol(mat)
        hijo.set_coste(find_cost(sol,hijo.get_datos())+loop)
        nodo.set_hijo(hijo)
    mat = move_right(nodo.get_datos())
    if(mat):
        hijo = NodoArbol(mat)
        hijo.set_coste(find_cost(sol,hijo.get_datos())+loop)
        nodo.set_hijo(hijo)
        
def find_cost(sol,estado):
    cont = 0
    for i in range(len(sol)):
        for j in range(len(sol[i])):
            if(sol[i][j] is not estado[i][j]):
                cont+=1
    return cont
            
def show(aux, aux2):
    print('Mover: (' + str(aux) + ', ' + str(aux2) + ') → (' + str(aux2) + ', ' + str(aux) + ')')























