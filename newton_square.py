# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:20:41 2011

@author: antoanne

http://en.wikipedia.org/wiki/Newton%27s_method
"""
import random, numpy

def iteracao(N, x):
    return float(x-(((x**2)-N)/(2*x)))

def iteraOnN(d, start, N):
    count = 0
    atual = 0
    x = start
    while (round(atual, d) <> round(x, d)):
        count += 1
        atual = x
        x = iteracao(N, x)
    return {'raiz':x, 'iteracoes':count}
   
def iteraOnNes(NMin, NMax, Total):
    Nes = sorted(random.sample(numpy.arange(NMin, NMax, 0.01), Total))
    arrayNes = []
    for N in Nes:
        start = random.sample(numpy.arange(0, N, 0.01), 1)[0]
        d2 = (iteraOnN(2, start, N))
        d6 = (iteraOnN(6, start, N))
        d10 = (iteraOnN(10, start, N))
        arrayNes.append({'N': N, 'start':start, 'raiz':d10['raiz'], 
                'i2':d2['iteracoes'],
                'i6':d6['iteracoes'],
                'i10':d10['iteracoes']
                })
    return arrayNes

# Main
results = iteraOnNes(1,1000,100)
print "N\ti2\ti6\ti10\tstart\traiz"
print "----------------------------------------------------------------------"
for r in results:
    print r['N'], '\t', r['i2'], '\t', r['i6'], '\t', r['i10'], '\t', r['start'], '\t', r['raiz']

i2Median = numpy.median([r['i2'] for r in results])
i6Median = numpy.median([r['i6'] for r in results])
i10Median = numpy.median([r['i10'] for r in results])

i2Deviation = numpy.std([r['i2'] for r in results])
i6Deviation = numpy.std([r['i6'] for r in results])
i10Deviation = numpy.std([r['i10'] for r in results])

print
print "        Média -> D2:%.3f, D6:%.3f, D10:%.3f" % (i2Median, i6Median, i10Median)
print "Desvio padrão -> D2:%.3f, D6:%.3f, D10:%.3f" % (i2Deviation, i6Deviation, i10Deviation)
print
print "obs.: DX equivale ao numero de casas decimais na aproximação"