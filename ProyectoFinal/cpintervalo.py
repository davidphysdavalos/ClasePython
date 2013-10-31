from intervalo import *

class CPIntervalo(object):
    '''
    Clase auxiliar en la construccion de intervalos complejos en coordenadas
    polares
    '''
    
    def __init__(self, mod, arg=None):
        
        '''
        Se define el intervalo complejo a partir de los modulos y las fases
        '''
        
        if arg is None:
            
            arg = Intervalo(0)
            
        if not isinstance(mod,Intervalo):
            
            mod=Intervalo(mod)
            
        if not isinstance(arg,Intervalo):
            
            arg=Intervalo(arg)
        
        
        self.mod = mod
        self.arg = arg
        
    def __repr__(self):
        return "CPIntervalo [{},{}]".format(self.mod,self.arg)
    
    def __str__(self):
        return "[{},{}]".format(self.mod,self.arg)

    def _repr_html_(self):
        reprn = "[{}, {}]".format(self.mod, self.arg)
        reprn = reprn.replace("inf", r"&infin;")
        return reprn
    
    def _repr_latex_(self):
        return "$[{}, {}]$".format(self.mod, self.arg)
    
    def __mul__(self,otro):
        
        if not isinstance(otro, CPIntervalo):
            
            otro=CPIntervalo(otro)
        
        return CPIntervalo(self.mod*otro.mod,self.arg+self.arg)
    
    def __add__(self,otro):
        
        if not isinstance(otro,CPIntervalo):
            
            otro=CPIntervalo(otro)
        
        
        valreal=self.mod*cos(self.arg)+otro.mod*cos(otro.arg)
              
        valimag=self.mod*sin(self.arg)+otro.mod*sin(otro.arg)
        
        return CPIntervalo(sqrt(valreal**2+valimag**2),arctan(valimag/valreal))
    
    def __neg__(self):
        
        return CPIntervalo(self.mod,self.arg+np.pi)
    
    def __sub__(self,otro):
        
        if not isinstance(otro,CPIntervalo):
            
            otro=CPIntervalo(otro)
        
        valreal=self.mod*cos(self.arg)-otro.mod*cos(otro.arg)
              
        valimag=self.mod*sin(self.arg)-otro.mod*sin(otro.arg)
        
        return CPIntervalo(sqrt(valreal**2+valimag**2),arctan(valimag/valreal))
        
        

    