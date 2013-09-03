import numpy as np

class Intervalo(object):
    def __init__(self, lo, hi=None):
        
        if hi is None:
            hi = lo
        
        if type(lo) is Intervalo:
            self.lo = lo.lo
            self.hi = lo.hi
        else:
            if lo > hi:
                hi, lo = lo, hi
            self.lo = lo
            self.hi = hi
        
        
    def __repr__(self):
        #return "Intervalo(%s, %s)" % (self.lo, self.hi)
        return "Intervalo({}, {})".format(self.lo, self.hi)
    
    def __str__(self):
        return "[{}, {}]".format(self.lo, self.hi)
        
    
    #def _repr_html_(self):
     #   return "[{}, {}]".format(self.lo, self.hi)
    
    def _repr_latex_(self): # Para el IPython notebook:
        return "$[{},{}]$".format(self.lo, self.hi)

    def __add__(self, otro):
        otro = Intervalo(otro)
        return Intervalo(self.lo + otro.lo, self.hi + otro.hi)
        
    def __radd__(self,otro):
        return (self + otro)
            
    def __neg__(self):
        return Intervalo(-self.hi,-self.lo)
    
    def __sub__(self, otro):
        otro = Intervalo(otro)
        return Intervalo(self.lo - otro.hi, self.hi - otro.lo)
    
    def __mul__(self,otro):
        otro = Intervalo(otro)
        mullo = self.lo*otro.lo
        mulhi = mullo
        
        if self.lo*otro.hi < mullo:
            mullo = self.lo*otro.hi
        if self.lo*otro.hi > mulhi:
            mulhi = self.lo*otro.hi
            
        if self.hi*otro.lo < mullo:
            mullo = self.hi*otro.lo
        if self.hi*otro.lo > mulhi:
            mulhi = self.hi*otro.lo
            
        if self.hi*otro.hi < mullo:
            mullo = self.hi*otro.hi
        if self.hi*otro.hi > mulhi:
            mulhi = self.hi*otro.hi
            
        return Intervalo(mullo, mulhi)
    
    
    def __div__(self, otro):
        
        inf = float("infinity")
        
        if (otro.hi < 0)  or (otro.lo > 0):
            print 1.0/otro.hi, 1.0/otro.lo
            recip = Intervalo(1.0/otro.hi, 1.0/otro.lo)
            print recip
            return self*recip
        
        else:
            if otro.hi == 0:
                recip = Intervalo(-inf,1.0/otro.lo)
                return self*recip
            elif otro.lo == 0:
                recip = Intervalo(1.0/otro.hi, inf)
                return self*recip
            else:
                return [self*Intervalo(-inf,1.0/otro.lo), self*Intervalo(1.0/otro.hi, inf)]

    def __lt__(self, otro):
        otro = Intervalo(otro)
        return (self.hi < otro.lo)
    
    def __le__(self, otro):
        otro = Intervalo(otro)
        return (self.hi <= otro.lo)
    
    def __eq__(self, otro):
        otro = Intervalo(otro)
        return (self.lo == otro.lo and self.hi == otro.hi)
    
    def __ne__(self, otro):
        otro = Intervalo(otro)
        return not(self == otro)
    
    def __ge__(self, otro):
        otro = Intervalo(otro)
        return self.lo >= otro.hi
    
    def __gt__(self, otro):
        otro = Intervalo(otro)
        return self.lo > otro.hi
    
    def intersect(self, otro):
        otro = Intervalo(otro)
        
        lo = max(self.lo, otro.lo)
        hi = min(self.hi,otro.hi)
            
        if lo <= hi:
            return Intervalo(lo,hi)
        else:
            return -1
    
    def union(self, otro):
        otro = Intervalo(otro)
        
        if self.intersect(otro) is not -1:
            lo = min(self.lo,otro.lo)
            hi = max(self.hi,otro.hi)
            return Intervalo(lo,hi)
        else:
            inter1 = Intervalo(min(self.lo,otro.lo), min(self.hi,otro.hi))
            inter2 = Intervalo(max(self.lo,otro.lo), max(self.hi,otro.hi))
            
            return [inter1,inter2]
        
    def hull(self,otro):
        otro = Intervalo(otro)
        
        lo = min(self.lo,otro.lo)
        hi = max(self.hi,otro.hi)
        return Intervalo(lo,hi)