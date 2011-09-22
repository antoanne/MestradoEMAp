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
e = 0.001

passouLimite = False
isPositivo = True
qtdTermosPositivos = 0
qtdTermosNegativos = 0
arrayPos = []
arrayNeg = []
plotSoma = []
n = 0
soma = 0
while (max((soma - L), (L - soma)) > e):
    n += 1
    if(isPositivo):
        qtdTermosPositivos += 1   
        soma += getTermo(getImpar(qtdTermosPositivos))
    else:
        qtdTermosNegativos += 1
        soma += getTermo(getPar(qtdTermosNegativos))
    plotSoma.append(soma)
    if (soma > L):
        if(isPositivo):
            arrayPos.append(qtdTermosPositivos)
        else:
            qtdTermosPositivos = 0
        isPositivo = False
    else:
        if(not isPositivo):
            arrayNeg.append(qtdTermosNegativos)
        else:
            qtdTermosNegativos = 0
        isPositivo = True

plot(plotSoma)
title("Harmônica Alternada \nL=%f e=%f".decode('utf-8') %(L,e))
xlabel("Termos somados: %d\nPOS: %s\nNEG: %s" % (n, arrayPos, arrayNeg))
axhspan(L+e, L-e, facecolor='g', alpha=0.5)
show()