import functions as ft
from nodoArbol import NodoArbol
from functools import cmp_to_key

print('Eight piece puzzle solver')
n = int(input('Input the number of row in the matrix → '))
m = int(input('Great, now input the number of columns for each row → '))

print('Now!, let\'s fill both matrix with data.\nFirst, our starting configuration: ')
initial_state = ft.fill_matrix(m,n)
print('\nAnd the expected result will be: ')
solution = ft.fill_matrix(m,n)
print('\nHere\'s how we ended up looking: ')
print('Initial state:\n',initial_state)
print('Solution:\n',solution)
print('\nLet\'s look for the solution, hang on tight...')

root = NodoArbol(initial_state)
found = False
queue = []
visited = []

loop = 1
while (not found) or len(queue) is not 0:
    if(root.get_data() == solution):
        found = True
        print('Solution found')
        print(ft.print_solution(root, solution, initial_state))
        break
    visited.append(root.get_data())
    ft.move_all(solution, root)
    for i in range(len(root.get_son())):
        if(not root.get_son()[i].get_data() in visited):
            if(not ft.in_queue(root.get_son()[i], queue)):
                queue.append(root.get_son()[i])
    queue = sorted(queue, key=cmp_to_key(ft.compare)) 
    root = queue.pop(0)
    loop +=1
print (loop)
 
        
        
        