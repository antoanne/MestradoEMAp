# -*- coding: utf-8 -*-
import csv

folderPath = '/home/antoanne/Dropbox/Work-2011/Mestrado/Probabilidade/'
#pSpamByPalavra = csv.DictReader(open(folderPath + 'learnedSpam.csv', 'rb'), delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#pNormalByPalavra = csv.DictReader(open(folderPath + 'learnedNormal.csv', 'rb'), delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

toTest = csv.DictReader(open(folderPath + 'testFull.csv', 'rb'), delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

palavras = toTest.fieldnames
palavras.pop(0)

probs = []
count = 0
for t in toTest:
    #print t
    probs = []
    for p in palavras:
        if int(t[p]) == 1:
            pSpamByPalavra = csv.DictReader(open(folderPath + 'learnedSpam.csv', 'rb'), delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for s in pSpamByPalavra:
                probs.append(s[p])
    #print 'calc', probs
    m = 0
    c = 0
    for v in probs:
        if m == 0:
            m = float(v)
        else:
            m *= float(v)
        
        if c == 0:
            c = float(float(1)-float(v))
        else:
            c *= float(float(1)-float(v))
    if (m <> 0 and c <> 0):
        P = m/(m+c)
        if (int(t[None][0])== 0) and (P > 0.5):
            print count, 'errado , é spam'
        elif (int(t[None][0])== 0) and (P <= 0.5):
            print count, 'correto, não é spam'
        elif (int(t[None][0])== 1) and (P > 0.5):
            print count, 'correto, é spam'
        elif (int(t[None][0])== 1) and (P <= 0.5):
            print count, 'errado , não é spam'
            
    count += 1