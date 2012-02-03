# -*- coding: utf-8 -*-
import random
#importa as funcoes zeros e mean do numpy
from numpy import zeros, mean

class Aviao:
    assentos = []
    #qnt de passageiros que sentaram fora do lugar
    fora = 0
    def __init__(self, qtdAssentos, posPrimeiro):
        self.assentos = zeros(qtdAssentos)
        self.assentos[posPrimeiro -1] = 1
    def senta(self, ordem):
        if (self.assentos[ordem -1] == 0) :
            #print "senta %d" % ordem
            self.assentos[ordem -1] = ordem
        else:
            #print "outro %d" % ordem
            #acrescenta 1 cada vez que um passageiro senta fora do lugar
            self.fora += 1
            self.encontraOutroAssento(ordem)
    def encontraOutroAssento(self, ordem):
        sentou = False
        while sentou == False:
            novoAssento = random.randrange(1, qtdAssentos + 1, 1)
            if self.assentos[novoAssento -1] == 0:
                self.assentos[novoAssento -1] = ordem
                sentou = True
        #print ordem
    def ultimoSentouCerto(self):
        return (self.assentos[qtdAssentos -1] == qtdAssentos)


def embarcaAviao():
    posPrimeiro = random.randrange(1, qtdAssentos + 1, 1)
    A = Aviao(qtdAssentos, posPrimeiro)
    x = 2
    while x < qtdAssentos + 1:
        A.senta(x)
        x += 1
    #variavel para receber a quantidade de passageiros fora de seus lugares     
    aux = A.fora 
    return A.ultimoSentouCerto(), aux

qtdAssentos = 100
testes = 100000
sucessos = 0
#lista para guardar a variavel aux de cada teste
qtdfora = []    
    
for n in range(1, testes + 1):
    # a recebe true ou false e b recebe a variavel aux
    a, b = embarcaAviao()
    sucessos += 1 if (a == True) else 0
    # appenda qntd de fora a cada teste
    qtdfora.append(b) 
    
print 'Probabilidade de que o passageiro de numero 100 sente-se em seu lugar: ', float(sucessos) / float(testes)

print 'Numero medio de passageiros que sentam fora de seus lugares: ', mean(qtdfora) 