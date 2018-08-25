from copy import deepcopy
from nodoArbol import NodoArbol

def move_up(mat):
    newMat = deepcopy(mat)
    tup = look_up(newMat)
    if(tup[0] == 0):
        return False
    else:
        aux = newMat[tup[0]-1][tup[1]]
        newMat[tup[0]-1][tup[1]] = newMat[tup[0]][tup[1]]
        newMat[tup[0]][tup[1]] = aux
        return newMat
    
def move_down(mat):
    newMat = deepcopy(mat)
    tup = look_up(newMat)
    if(tup[0] == (len(newMat)-1)):
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
    if(tup[1]==(len(newMat[0])-1)):
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
            
def move_all(sol, nodo):
    mat = move_up(nodo.get_datos())
    if(mat):
        append_son(nodo, mat, sol)
        
    mat = move_down(nodo.get_datos())
    if(mat):
        append_son(nodo, mat, sol)
            
    mat = move_left(nodo.get_datos())
    if(mat):
        append_son(nodo, mat, sol)
            
    mat = move_right(nodo.get_datos())
    if(mat):
        append_son(nodo, mat, sol)
        
def find_cost(sol, estado):
    cont = 0
    for i in range(len(sol)):
        for j in range(len(sol[i])):
            if(not(sol[i][j] == estado[i][j])):
                if((estado[i][j] is not 0) and (sol[i][j] is not 0)):
                    cont+=1
    return cont
            
def append_son(nodo, mat, sol):
        hijo = NodoArbol(mat)
        hijo.set_padre(nodo)
        hijo.set_step(nodo.get_step()+1)
        hijo.set_coste(find_cost(sol, hijo.get_datos()) + hijo.get_step())
        nodo.set_hijo(hijo)

    
def move_instruction(aux, aux2):
    print('Mover: (' + str(aux) + ', ' + str(aux2) + ') → (' + str(aux2) + ', ' + str(aux) + ')')




















