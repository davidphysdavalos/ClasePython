from intervalo import *

class CIntervalo(object):
    '''
    Clase auxiliar en la construccion de intervalos complejos
    '''
    def __init__(self, re, im=None):
        
        if im is None:
            im = Intervalo(0)
            
        if not isinstance(re,Intervalo):
            
            re=Intervalo(re)
            
        if not isinstance(im,Intervalo):
            
            im=Intervalo(im)
        
        
        self.re = re
        self.im = im
        
    def __repr__(self):
        return "CIntervalo [{},{}]".format(self.re,self.im)
    
    def __str__(self):
        return "[{},{}]".format(self.re,self.im)

    def _repr_html_(self):
        reprn = "[{}, {}]".format(self.re, self.im)
        reprn = reprn.replace("inf", r"&infin;")
        return reprn
    
    def _repr_latex_(self):
        return "$[{}, {}]$".format(self.re, self.im)
    
    def __mul__(self,otro):
        
        if not isinstance(otro, CIntervalo):
            
            otro=CIntervalo(otro)
        
        return CIntervalo(self.re*otro.re-self.im*otro.im, self.im*otro.re+otro.im* self.re)
    
    def __rmul__(self, otro):
        
        return self*otro
        
    def __radd__(self, otro):
        
        return self + otro
    
    def __add__(self,otro):
        
        if not isinstance(otro, CIntervalo):
            
            otro=CIntervalo(otro)
        
        return CIntervalo(self.re+otro.re,self.im+otro.im)
    
    def abs(self):
     
        #return CIntervalo(sqrt(self.re**2+self.im**2))
        
        return math.sqrt(self.re.abs()**2+self.im.abs()**2)
        
    
    def __div__(self,otro):
        
        if not isinstance(otro, CIntervalo):
            
            otro=CIntervalo(otro)
        
        otroc= otro.conjugate()
        
        ab=otro.abs()
        
        cociente=ab**(-2.0)
        
        return (self*otroc)*cociente
    
    def __rdiv__(self,otro):
            
        return self/otro
        
    def __neg__(self):
        
        return CIntervalo(-self.re, -self.im)
        
    def __sub__(self, otro):
        
        if not isinstance(otro, CIntervalo):
            
            otro=CIntervalo
        
        return CIntervalo(self.re-otro.re, self.im-otro.im)
        
    def exp(self):
        
        aux=CIntervalo(exp(self.re))        
        
        return aux*CIntervalo(cos(self.im), sin(self.im))
        
    #def __pow__(self,otro):
        
        
    ##Estas funciones jalan bien... creo ####
        
        
    def __and__(self,otro):
        
        if self.re & otro.re==None:
            
            return None
            
        if self.im & otro.im==None:
            
            return None
        
        return CIntervalo(self.re & otro.re, self.im & otro.im)
        
    def __contains__(self, otro):
        

        if not isinstance(otro, CIntervalo):
            
            otro=CIntervalo(otro)

            
        return otro & self == otro 
    
    
    def conjugate(self):
    
        return CIntervalo(self.re,-self.im)


    def middle(self):
    
        return CIntervalo(self.re.middle(),self.im.middle())
    
    
    ##Funciones en construccion ######
    
    def __arg__(self):
    
        return CIntervalo(0, arctan(self.im/self.re))
        
        
    
    
