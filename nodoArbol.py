class NodoArbol(object):
    def __init__(self, datos, hijo=None):
        self.datos = datos
        self.hijo = []
        if(hijo):
            self.hijo.append(hijo)
        self.padre = None
        self.coste = None
    
    def set_hijo(self, hijo):
        self.hijo.append(hijo)
        hijo.set_padre(self)
    
    def get_hijo(self):
        return self.hijo
    
    def get_padre(self):
        return self.padre
    
    def set_padre(self, padre):
        self.padre = padre
    
    def set_datos(self, datos):
        self.datos = datos
    
    def get_datos(self):
        return self.datos
    
    def set_coste(self, coste):
        self.coste = coste
    
    def get_coste(self):
        return self.coste
    
    def igual(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False
    
    def en_lista(self, lista_nodos):
        en_la_lista = False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista = True
        return en_la_lista
    
    def __str__(self):
        return str(self.get_datos())