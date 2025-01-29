import math

def complxsuma (a,b):
    real = (a[0]+b[0])
    imaginario = (a[1]+b[1])
    return (f"el resultado de la suma de los numeros complejos es :{real},{imaginario}i")
def complxproducto (a,b):
    real = (a[0]*b[0]-a[1]*b[1])
    imaginario = (a[0]*b[1]+b[0]*a[1])
    return (f"el resultado del producto de los numeros complejos es :{real},{imaginario}i")
def complxresta (a,b):
    real = (a[0]-b[0])
    imaginario = (a[1]-b[1])
    return (f"el resultado de la resta de los numeros complejos es :{real},{imaginario}i")
def complxdivision (a,b):
    if b == (0,0):
        return ("no se puede hacer")
    else:
        divisor= (b[0]**2)+(b[1]**2)
        real = (a[0]*b[0]+a[1]*b[1])/divisor
        imaginario = (b[0]*a[1]-a[0]*b[1])/divisor
    return (f"el resultado de la division de los numeros complejos es :{real},{imaginario}i")
def complxmodulo (a):
    if a == (0,0):
        return ("no se puede hacer")
    else:
        elevados = (a[0]**2+a[1]**2)
        raiz = elevados**0.5
        return (f"el resultado del modulo de tu numero complejo es {raiz}")
def complxconjugado (a):
    real= a[0]
    imaginario = -a[1]
    return (f"el resultado del conjugado de tu numero complejo es {real},{imaginario}i")

def complxpolarcarter (a):
    real = a[0]*math.cos(a[1])
    real1 = round(real,5)
    imaginario = a[0]*math.sin(a[1])
    imaginario1 = round(imaginario,5)
    return (f"al pasar de polar a carteciano tu numero complejo el resultado es {real1},{imaginario1}i")
def complxcarterpolar (a):
    if a[0] == 0:
        return ("no se puede hacer")
    else:
        elevados = (a[0]**2+a[1]**2)
        ro = elevados**0.5
        angulo = math.atan(a[1]/a[0])
        angulo1 = (angulo*180)/math.pi
        return (f"al pasar de carteciano a polar tu nuevo conjunto polar tiene un ro:{ro}, y un angulo {angulo1}")
def complxfase (a):
    fase = math.atan(a[1]/a[0])
    fase1 =  round(fase,5)
    return (f"el valor de la fase de ese numero complejo es:{fase1}")






