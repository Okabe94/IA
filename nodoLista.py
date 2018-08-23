class NodoLista(object):
    def __init__(self, datos):
        self.datos = datos
        self.next = None
        self.previous = None
        self.upper = None
        self.lower = None
        
    def get_datos(self):
        return self.datos
    
    def get_next(self):
        return self.next
    
    def get_previous(self):
        return self.previous
    
    def get_upper(self):
        return self.upper
    
    def get_lower(self):
        return self.lower
    
    def set_datos(self,datos):
        self.datos = datos
        
    def set_next(self,n):
        self.next = n
        
    def set_previous(self,p):
        self.previous = p
        
    def set_upper(self,u):
        self.upper = u
            
    def set_lower(self,l):
        self.lower = l