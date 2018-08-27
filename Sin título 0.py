import functions as ft
from nodoArbol import NodoArbol
from functools import cmp_to_key

#def lowest_cost(root):
#    lis = root.get_son()
#    if(not lis):
#        return False
#    cost = lis[0].get_cost()
#    nodo = lis[0]
#    for i in lis:
#        if(i.get_cost() < cost):
#            cost = i.get_cost()
#            nodo = i
#    return nodo
        
def tree(root):
    steps = 0
    while (root is not None):
        print(root.get_data())
        root = root.get_father()
        print(steps)
        steps+=1
        print()
        
def vis(visited):
    for i in range(len(visited)):
        print(visited[i].get_data())
    
def que(queue):
    for i in range(len(queue)):
        print(queue[i].get_data())
        
def compare(x,y):
    c1 = x.get_cost()
    c2 = y.get_cost()
    return c1 - c2

def comp(x, y):
    c1 = x.get_cost()
    c2 = y.get_cost()
    return c2 - c1

def in_visited(nodo, visited):
    for i in range(len(visited)):
        if(nodo.get_data() == visited[i].get_data()):
            return True
    else:
        return False
    
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
#sort it and pop the lowest cost
#the one that was popped add it to the visited list
#rinse and repeat until there are none left in the queue 


root = NodoArbol(initial_state)
loop = 1
found = False
queue = []
visited = []

while (not found) or len(queue) is not 0:
#    if(not found):
#        if(root.get_data() == solution):
#            found = True
#            print('Solution found')
#            result = root
#    else:
#        if(root.get_step() >= result.get_step()):
#            if(queue):
#                root = queue.pop(0)
#            else:
#                break
#        else:
#            if(root.get_data() == result.get_data()):
#                    result = root
#    if(not root.get_data() == solution):
    if(root.get_data() == solution):
        found = True
        print('Solution found')
        tree(root)
        break
    visited.append(root.get_data())
    ft.move_all(solution, root)
   # root.son = sorted(root.get_son(), key=cmp_to_key(comp))
    for i in range(len(root.get_son())):
        if(not root.get_son()[i].get_data() in visited):
            if(not in_queue(root.get_son()[i], queue)):
                queue.append(root.get_son()[i])
    queue = sorted(queue, key=cmp_to_key(compare)) #lowest to greatest
    root = queue.pop(0)
        #queue = sorted(queue, key=cmp_to_key(compare))
        #visited.append(root)
    loop+=1

    
#sort the queue list from lowest to greatest
#take care of the queue list so it only adds the lowest cost configuration
#before adding to queue list make sure the one in there has a lowest cost
#no need to keep the loop going after finding a solution 
#it should be the fastest one by definition       







 
        