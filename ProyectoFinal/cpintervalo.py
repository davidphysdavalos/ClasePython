from intervalo import *

import numpy as np

math=np

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
        #self.arg = math.mod(arg, 2*math.pi)
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
        
        return CPIntervalo(self.mod*otro.mod,self.arg+otro.arg)
        
    def __rmul__(self, otro):
        
        return self*otro
        
    def __radd__(self, otro):
        
        return self+otro
        
    def __rsub__(self, otro):
        
        return self-otro
        
    def __rdiv__(self, otro):
        
        return self/otro
        
    
    def __add__(self,otro):
        
        if not isinstance(otro,CPIntervalo):
            
            otro=CPIntervalo(otro)
        
        
        valreal=self.mod*cos(self.arg)+otro.mod*cos(otro.arg)
              
        valimag=self.mod*sin(self.arg)+otro.mod*sin(otro.arg)
        
        return CPIntervalo(sqrt(valreal**2+valimag**2),arctan(valimag/valreal))
        
    def __contains__(self, otro):

        return otro & self == otro 

    
    def __neg__(self):
        
        return CPIntervalo(self.mod,self.arg+math.pi)
    
    def __sub__(self,otro):
        
        if not isinstance(otro,CPIntervalo):
            
            otro=CPIntervalo(otro)
        
        valreal=self.mod*cos(self.arg)-otro.mod*cos(otro.arg)
              
        valimag=self.mod*sin(self.arg)-otro.mod*sin(otro.arg)
        
        return CPIntervalo(sqrt(valreal**2+valimag**2),arctan(valimag/valreal))
        
    def __div__(self,otro):
        
        if not isinstance(otro, CPIntervalo):
            
            otro=CPIntervalo(otro)
        
        return CPIntervalo(self.mod/otro.mod,self.arg-otro.arg)
        
        
    def log(self):
        
        modulo=sqrt(log(self.mod)**2+self.arg**2)
        
        argumento=arctan(self.arg/(log(self.mod)))
        
        return CPIntervalo(modulo, argumento)
        
        
    def exp(self):
        
        return CPIntervalo(exp(self.mod*cos(self.arg)), self.mod*sin(self.arg))
        
    def __pow__(self, otro):
        
        if not isinstance(otro, CPIntervalo):
            
            otro=CPIntervalo(otro)
        
        aux=log(self)        
        
        return exp(otro*aux)
        
    def __rpow__(self, otro):
        
        if not isinstance(otro, CPIntervalo):
            
            otro=CPIntervalo(otro)
            
        return otro**self
        
    def __and__(self, otro):
        
        if not isinstance(otro,CPIntervalo):
            otro = CPIntervalo(otro)
            
        if (self.mod.lo > otro.mod.hi) | (self.mod.hi < otro.mod.lo):
            return None
            
        if (self.arg.lo > otro.arg.hi) | (self.arg.hi < otro.arg.lo):
            return None

        else:
            a = max( self.mod.lo, otro.mod.lo )
            b = min( self.mod.hi, otro.mod.hi )
            c = max( self.arg.lo, otro.arg.lo )
            d = min( self.arg.hi, otro.arg.hi )
        return CPIntervalo(Intervalo(a,b),Intervalo(c,d))
        
        
        
    def middle(self):
        
        r=(self.mod.lo+self.mod.hi)*0.5
        
        theta=(self.arg.lo+self.arg.hi)*0.5
        
        return r*math.cos(theta)+r*math.sin(theta)*1j 
        
    #El seno y el coseno ya dan los valores bien por lo menos para intervalos
    #degenerados, lo demas depende si estan bien definidas las operaciones
    #en la clase intervalo        
        
    def cos(self):
        
        caux=self.mod*cos(self.arg)
        
        saux=self.mod*sin(self.arg)
        
        return (exp(CPIntervalo(-saux))*CPIntervalo(1.0, caux)+\
        
        exp(CPIntervalo(saux))*CPIntervalo(1.0,-caux))*0.5
        
    def sin(self):
        
        return cos(self-CPIntervalo(math.pi*0.5))