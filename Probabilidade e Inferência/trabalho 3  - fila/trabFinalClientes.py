# -*- coding: utf-8 -*-
from numpy import *
import random
qtdMaxClientes = 10000
tempoAtendimentoPorCliente = zeros(qtdMaxClientes)
atendimentos = []
qtdAtendentes = 2
clientesAtendidos = 0

# cria fila de atendimentos
while clientesAtendidos < qtdMaxClientes:
    # chegada de clientes cada 10min
    qtdClientesAgora = poisson(1)
    if (qtdClientesAgora > 0):
        clientes = []
        #para cada cliente deste 10min
        mediaAtendimento10min = 0
        tempoEspera10min = 0
        for c in range(0, qtdClientesAgora):
            if (random.randrange(1, 11, 1) < 5):
                x = random.randrange(2, 4.01, 0.01, float)
                tempo = (1 - abs(x - 3))
            else:
                tempo = exponential(7.0)
            clientes.append(tempo)
        clientesAtendidos += qtdClientesAgora
        atendimentos.append(clientes)
        
print "quantidade de intervalos de tempo com 10 minutos é", len(atendimentos)

#separar cada atendimento pela quantidade de atendentes
atendimentosPorFila = []
posicao = 0
for atendimento in atendimentos:
   atendimentosPorFila.append([])
   #inicia as filas
   filas = []
   for x in range(0, qtdAtendentes):
       filas.append([0])
   for a in atendimento:
       maisRapido = 0
       #identifica a fila mais rápida neste momento
       count = 0
       for fila in filas:
           if (sum(fila) < sum(filas[maisRapido])):
               maisRapido = count
           count += 1
       if (filas[maisRapido] == [0]):
           filas[maisRapido] = [a]
       else:
           filas[maisRapido].append(a)
   atendimentosPorFila[posicao] = filas
   posicao += 1
   
#calcula media das filas
mais3min = 0
medias = []
for atendimento in atendimentosPorFila:
    media = 0.0
    for a in atendimento:
        for x in range(0,len(a)-1):
            if len(a) > 1:
                media += float(a[x+1])
                if a[x+1] > 0.0:
                    mais3min += 1
        media = media/float(len(atendimento))
    media = media/float(qtdAtendentes)
    medias.append(float(media))
print "média de tempo de espera para atendimento é %.2f" % (sum(medias)/len(medias))
print "clientes que esperam mais de 3 minutos %.2f%%" % ((float(mais3min) / qtdMaxClientes) * 100)
