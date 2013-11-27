import mpmath as math
import difauto

def default_color_function(ctx, z):
    if math.isinf(z):
        return (1.0, 1.0, 1.0)
    if math.isnan(z):
        return (0.5, 0.5, 0.5)
    pi = 3.1415926535898
    a = (float(math.arg(z)) + math.pi) / (2*math.pi)
    a = (a + 0.5) % 1.0
    b = 1.0 - float(1/(1.0+abs(z)**0.3))
    return hls_to_rgb(a, b, 0.8)


def de(n,k):
    result = 0
    
    j = n
    while j >= k:
        suma = (4**j)*(math.fac(n+j-1)/(math.fac(n-j)*math.fac(2*j)))
        result += suma
        j -= 1
    result *= n
    
    return result

def zeta(s,deriv=0):
    sigma = s.real
    t = s.imag
    d = math.mp.dps
    
    n = int(1.3*d + 0.9*abs(t))

    if deriv == 1:
        result = difauto.DifAuto(0,0)
        s = difauto.DifAuto(s,1)
    else:
        result = 0

    k = n
    while k >= 1:
        suma = (-1)**(k-1) * de(n,k) / (k**s)
        result += suma
        k -= 1
   
    result *= (1/(de(n,0)*(1-2**(1-s))))
    return result

def xi(s, deriv = 0):
    result = math.gamma(0.5*s)*math.zeta(s)*(math.pi**(s/2.))*(1-s)*s/2.
    return result

def theta(t):
    result = (t/2.)*math.log(t/(2.*math.pi)) - t/2. - math.pi/8. + 1/(48.*t) + 7/(5760.*(t**3))
    return result

def phi0(z):
    result = math.cos(0.5*math.pi*(z**2) + 3*math.pi/8)/math.cos(math.pi*z)
    return result

def siegelz(t):
    try:
        tao = sqrt(t.hi)
    except:
        tao = math.sqrt(t)

    tao = tao/math.sqrt(2*math.pi)
    m = int(tao)
    z = 2*(t-m) - 1

    result = 2*math.cos(theta(t))

    n = 2
    
    while n <= m:
        result = result + 2*math.cos(theta(t) - t*math.log(n))/math.sqrt(n)
        n = n + 1

    result  = result + (-1)**(m+1)*(1/(math.sqrt(tao)))*(phi0(z) - (phi0(z)**3)/(12.*tao*(math.pi**2)))
    return result

