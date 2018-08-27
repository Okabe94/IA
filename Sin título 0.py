import functions as ft
from nodoArbol import NodoArbol
from functools import cmp_to_key

def tree(root):
    steps = 0
    while (root is not None):
        print(root.get_data())
        root = root.get_father()
        print(steps)
        steps+=1
        print()

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

initial_state = [[3,2,4],[7,6,8],[5,0,1]]
# [0,3,7]
# [4,2,5]
# [6,1,8]
           
solution = [[1,2,3],[4,5,6],[7,8,0]]
# [0,1,2]
# [3,4,5]
# [6,7,8]

root = NodoArbol(initial_state)
loop = 1
found = False
queue = []
visited = []

while (not found) or len(queue) is not 0:
    if(root.get_data() == solution):
        found = True
        print('Solution found')
        tree(root)
        break
    visited.append(root.get_data())
    ft.move_all(solution, root)
    for i in range(len(root.get_son())):
        if(not root.get_son()[i].get_data() in visited):
            if(not in_queue(root.get_son()[i], queue)):
                queue.append(root.get_son()[i])
    queue = sorted(queue, key=cmp_to_key(compare)) 
    root = queue.pop(0)
    loop+=1

 
        
        
        