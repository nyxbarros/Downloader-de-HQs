class Lista(list):
    def map(self, func):
        return Lista(func(x) for x in self)
    
    def filter(self, func):
        lista = []
        for i in self:
            if func(i):
                lista.append(i)
        return Lista(lista)