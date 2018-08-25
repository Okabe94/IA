import functions as ft
from nodoArbol import NodoArbol
from functools import cmp_to_key

#def lower_cost(root):
#    lis = root.get_hijo()
#    if(not lis):
#        return False
#    cost = lis[0].get_coste()
#    nodo = lis[0]
#    for i in lis:
#        if(i.get_coste() < cost):
#            cost = i.get_coste()
#            nodo = i
#    return nodo
        
def tree(root):
    steps = 0
    while (root is not None):
        print(root.get_datos())
        root = root.get_padre()
        print(steps)
        steps+=1
        print()
        
def vis(visited):
    for i in range(len(visited)):
        print(visited[i].get_datos())
    
def que(queue):
    for i in range(len(queue)):
        print(queue[i].get_datos())
        
def compare(x,y):
    c1 = x.get_coste()
    c2 = y.get_coste()
    return c1 - c2

def comp(x, y):
    c1 = x.get_coste()
    c2 = y.get_coste()
    return c2 - c1

def in_visited(nodo, visited):
    for i in range(len(visited)):
        if(nodo.get_datos() == visited[i].get_datos()):
            return True
    else:
        return False
    
def in_queue(nodo, queue):
    for i in range(len(queue)):
        if(nodo.get_datos() == queue[i].get_datos()):
            return True
    else:
        return False

initial_state = [[0,3,7],[4,2,5],[6,1,8]]
# [0,3,7]
# [4,2,5]
# [6,1,8]
           
solution = [[0,1,2],[3,4,5],[6,7,8]]
# [0,1,2]
# [3,4,5]
# [6,7,8]

#move_all → gives me sons
#next add those to the queue list
#sort it and pop the lower cost
#the one that was popped add it to the visited list
#rinse and repeat until there are none left in the queue 


root = NodoArbol(initial_state)
loop = 1
found = False
queue = []
visited = []

while (not found) or (queue):
    if(not found):
        if(root.get_datos() == solution):
            found = True
            print('Solution found')
            result = root
            #When found gotta keep looking for a better solution
            #could: have an if statement inside checking found and comparing cost
            #       changing the node if the cost is lower and the solution is found
    else:
        if(root.get_step() >= result.get_step()):
            if(queue):
                root = queue.pop(0)
            else:
                break
        else:
            if(root.get_datos() == result.get_datos()):
                    result = root
    if(not root.get_datos() == solution):
        visited.append(root.get_datos())
    ft.move_all(solution, root)
        #node with children attached, need the one with lower cost
        #before queuing them check on visited not to duplicate data
        #could: sort the son list or leave it as is and look for the lower one
    root.hijo = sorted(root.get_hijo(), key=cmp_to_key(comp))
    for i in range(len(root.get_hijo())):
        if(not root.get_hijo()[i].get_datos() in visited):
            if(not in_queue(root.get_hijo()[i], queue)):
                queue.insert(0, root.get_hijo()[i])
#        for i in root.get_hijo():
#            if(in_visited(i,visited)):
#                queue.append(i)
    if(not found):
        root = queue.pop(0)
        #queue = sorted(queue, key=cmp_to_key(compare))
        #visited.append(root)
    loop+=1
tree(result)
    

        
        