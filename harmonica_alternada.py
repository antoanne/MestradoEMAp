# -*- coding: utf-8 -*-
"""
@author: Antoanne Pontes
"""
from matplotlib.pyplot import plot, title, show, axhspan, xlabel

# programador way
#def getTermo(n):
#    if (int(n) % 2 == 0):
#        return float(-(1.0/float(n)))
#    else:
#        return float(1.0/float(n))
# matemático way
def getTermo(n):
    return float(((-1)**(float(n)+1))*(1/float(n)))

def getPar(n):
    return int((n*1)+n)

def getImpar(n):
    return int(getPar(n)-1)

# Entradas
L = 2
e = 0.01

n = 0
soma = 0
plotSoma = []
arrayPos = []
arrayNeg = []
ponteiroPos = 0
ponteiroNeg = 0
qtdTermosPositivos = 0
qtdTermosNegativos = 0
isPositivo = True
while (True):
    n += 1
    if (isPositivo):
        qtdTermosPositivos += 1
        soma += getTermo(getImpar(qtdTermosPositivos))
        ponteiroPos = soma
    else:
        qtdTermosNegativos += 1
        soma += getTermo(getPar(qtdTermosNegativos))
        ponteiroNeg = soma
    plotSoma.append(soma)
    if (soma > L):
        if(isPositivo):
            arrayPos.append(qtdTermosPositivos)
        isPositivo = False
    else:
        if(not isPositivo):
            arrayNeg.append(qtdTermosNegativos)
        isPositivo = True
    if (((ponteiroPos > L) and (ponteiroPos < L+e)) and ((ponteiroNeg < L) and (ponteiroNeg > L-e))):
        break

print arrayPos, arrayNeg
title("Harmônica Alternada \nL=%.10f e=%.10f".decode('utf-8') %(L,e))
xlabel("Total de termos somados: %d\nPOS: %s || NEG: %s" % (n, qtdTermosPositivos, qtdTermosNegativos))
axhspan(L+e, L-e, facecolor='g', alpha=0.5)
plot(plotSoma)
show()