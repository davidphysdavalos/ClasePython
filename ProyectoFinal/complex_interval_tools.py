import cpintervalo as cpi
import cintervalo as ci


def polar2cart(x):
    
    if not isinstance(x, cpi.CPIntervalo):
        
        print 'Esto no es un intervalo en coordenadas polares'
        
        return None
    
    return ci.CIntervalo(x.mod*cpi.cos(x.arg), x.mod*cpi.sin(x.arg))
    
def cart2polar(x):
    
    if not isinstance(x, ci.CIntervalo):
        
        print 'Esto no es un intervalo en coordenadas cartesianas'
        
        return None
    
    return cpi.CPIntervalo(x.abs(), x.arg())
    
    