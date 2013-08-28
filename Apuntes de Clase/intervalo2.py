class Intervalo(object):
    #Docstring
    '''
    Esta Clase provee aritmetica de Intervalos
    '''
    def __init__(self,min,max=None):
        if max is None:
            max=min
            
        self.min=min
        self.max=max
    
    #def __repr__(self):
        #return 'Intervalo(%s,%s)' %(self.min,self.max)
        #Otra manera:
        #return 'Intervalo({},{})'.format(self.min,self.max)
    #def __str__(self):
        #return '[{},{}]'.format(self.min,self.max)
    #Para el Ipython
    #def _repr_html_(self):
        #return '[{},{}]'.format(self.min,self.max)
    #En LaTeX
    def _repr_latex_(self):
        return '$[{},{}]$'.format(self.min,self.max)
    
    def __add__(self,otro):
        
        return Intervalo(self.min+otro.min,self.max+otro.max)