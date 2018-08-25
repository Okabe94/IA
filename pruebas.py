from nodoArbol import NodoArbol
from copy import deepcopy

hola = NodoArbol(2)
new = NodoArbol(19)
hola.set_hijo(new)
e = hola
hola = NodoArbol(22)

print (e.get_hijo()[0].get_datos())
print(hola.get_hijo()[0].get_datos())