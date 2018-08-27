class NodoArbol(object):
    def __init__(self, data, son=None):
        self.data = data
        self.son = []
        if(son):
            self.son.append(son)
        self.father = None
        self.cost = 0
        self.step = 1
        self.move = None
    
    def set_son(self, son):
        self.son.append(son)
    
    def get_son(self):
        return self.son
    
    def get_father(self):
        return self.father
    
    def set_father(self, father):
        self.father = father
    
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    def set_cost(self, cost):
        self.cost = cost
    
    def get_cost(self):
        return self.cost
    
    def set_step(self, step):
        self.step = step
        
    def get_step(self):
        return self.step

    def set_move(self, move):
        self.move = move
    
    def get_move(self):
        return self.move