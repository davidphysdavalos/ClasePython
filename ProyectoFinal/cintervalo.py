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
        
        return sqrt(self.re**2+self.im**2)
        
    
    def __div__(self,otro):
        
        if not isinstance(otro, CIntervalo):
            
            otro=CIntervalo(otro)
        
        denominator=otro.abs()**2
        
        numeradorReal= self.re*otro.re+self.im*otro.im
        
        numeradorcomplex = self.im*otro.re-otro.im*self.re
        
        return CIntervalo(numeradorReal/denominator, numeradorcomplex/denominator)
    
    def __rdiv__(self,otro):
            
        return self/otro
        
    def __neg__(self):
        
        return CIntervalo(-self.re, -self.im)
        
    def __sub__(self, otro):
        
        if not isinstance(otro, CIntervalo):
            
            otro=CIntervalo(otro)
        
        return CIntervalo(self.re-otro.re, self.im-otro.im)
        
    def __rsub__(self, otro):
        
        return self-otro
        
    def exp(self):
        
        aux=CIntervalo(exp(self.re))        
        
        return aux*CIntervalo(cos(self.im), sin(self.im))
        
    def log(self):
        
        return CIntervalo(log(self.abs()), self.arg())
        
    def __pow__(self,otro):
        
        auxlog=log(self)
        
        aux= otro*auxlog
        
        a=exp(aux)
        
        return a
        
    def __rpow__(self, otro):
        
        if not isinstance(otro, CIntervalo):
            
            otro=CIntervalo(otro)
            
        return otro**self
        
        
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
    
    def arg(self):
    
    
        return arctan(self.im/self.re)
        
    ### Trigonometric Functions
        
    def sin(self):
        
        return CIntervalo(cosh(self.im)*sin(self.re), cos(self.re)*sinh(self.im))
        
    def cos(self):
        
        return sin(self+math.pi*0.5)
        
    def tan(self):
        
        return sin(self)/cos(self)
        
        
    
    
