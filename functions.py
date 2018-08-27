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
    mat = move_up(nodo.get_data())
    if(mat):
        append_son(nodo, mat, sol, 'Move Up')
        
    mat = move_down(nodo.get_data())
    if(mat):
        append_son(nodo, mat, sol, 'Move Down')
            
    mat = move_left(nodo.get_data())
    if(mat):
        append_son(nodo, mat, sol, 'Move Left')
            
    mat = move_right(nodo.get_data())
    if(mat):
        append_son(nodo, mat, sol, 'Move Right')
        
def find_cost(sol, estado):
    cont = 0
    for i in range(len(sol)):
        for j in range(len(sol[i])):
            if(not(sol[i][j] == estado[i][j])):
                if((estado[i][j] is not 0) and (sol[i][j] is not 0)):
                    cont+=1
    return cont
            
def append_son(nodo, mat, sol, move):
        son = NodoArbol(mat)
        son.set_father(nodo)
        son.set_step(nodo.get_step()+1)
        son.set_cost(find_cost(sol, son.get_data()) + son.get_step())
        son.set_move(move)
        nodo.set_son(son)

def print_solution(root, solution, initial_state):
    print('Solution: ', solution)
    print('Initial state: ',initial_state)
    print('\nList of Movements:\n')
    #root = root.get_father()
    result = ''
    if(root is None):
        return 'No moves required'
    while (root is not None):
        result = '-  '+ str(root.get_move()) + '\n' + result
        root = root.get_father()
    return result

def compare(x,y):
    c1 = x.get_cost()
    c2 = y.get_cost()
    return c1 - c2
    
def in_queue(nodo, queue):
    for i in range(len(queue)):
        if(nodo.get_data() == queue[i].get_data()):
            if(nodo.get_cost() < queue[i].get_cost()):
                queue.remove(queue[i])
                return False
            else:
                return True
    else:
        return False

def fill_matrix(mat):
    for i in range(len(mat)):
        print('Values for row number: ' + str(i+1))
        for j in range(len(mat[i])):
            value = input('Input value for cell [' + str(i+1) + '][' + str(j+1) + '] → ')
            if(value in ''):
                print('Oops!, slight mistake, let\'s do that again please')
                mat[i][j] = int(input('Input value for cell [' + str(i+1) + '][' + str(j+1) + '] → '))
            else:
                mat[i][j] = int(value)
          















