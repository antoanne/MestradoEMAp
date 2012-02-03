# -*- coding: utf-8 -*-
import csv

folderPath = '/home/antoanne/Dropbox/Work-2011/Mestrado/Probabilidade/'
spamReader = csv.DictReader(open(folderPath + 'spamFull.csv', 'rb'), delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

qtdSpam = 0
qtdNormal = 0

for x in spamReader:
    if (x['spam']=='0'):
        qtdNormal += 1
    else:
        qtdSpam += 1

pQQSerSpam = float(qtdSpam) / float(qtdSpam+qtdNormal)
pQQNaoSpam = float(qtdNormal) / float(qtdSpam+qtdNormal)


palavras = spamReader.fieldnames
palavras.pop(0)
palavrasSpamDict = {}
palavrasNormalDict = {}
probPalavrasSpamDict = {}
probPalavrasNormalDict = {}
probSpamSobreTotal = {}
probNormalSobreTotal = {}
pSpamByPalavra = {}
pNormalByPalavra = {}

for x in palavras:
    palavrasSpamDict[x] = 0.0
    palavrasNormalDict[x] = 0.0
    probPalavrasSpamDict[x] = 0.0
    probPalavrasNormalDict[x] = 0.0
    probSpamSobreTotal[x] = 0.0
    probNormalSobreTotal[x] = 0.0
    pSpamByPalavra[x] = 0.0
    pNormalByPalavra[x] = 0.0

spamReader = csv.DictReader(open(folderPath + 'spamFull.csv', 'rb'), delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for x in spamReader:
    if (x['spam'] == '0'):
        for p in palavras:
            palavrasNormalDict[p] += float(x[p])
    else:
        for p in palavras:
            palavrasSpamDict[p] += float(x[p])

print palavrasSpamDict
print
print palavrasNormalDict

for p in palavras:
    probPalavrasSpamDict[p] = float(palavrasSpamDict[p])/float(qtdSpam)
    probPalavrasNormalDict[p] = float(palavrasNormalDict[p])/float(qtdNormal)
    probSpamSobreTotal[p] = float(probPalavrasSpamDict[p]) * float(pQQSerSpam)
    probNormalSobreTotal[p] = float(probPalavrasNormalDict[p]) * float(pQQNaoSpam)
    pSpamByPalavra[p] = float(probSpamSobreTotal[p]) / float(probSpamSobreTotal[p]+probNormalSobreTotal[p])
    pNormalByPalavra[p] = float(probNormalSobreTotal[p]) / float(probSpamSobreTotal[p]+probNormalSobreTotal[p])
    
print 'probSpam', probPalavrasSpamDict['make'], probSpamSobreTotal['make'], pSpamByPalavra['make']
print
print 'probNormal', probPalavrasNormalDict['make'], probNormalSobreTotal['make'], pNormalByPalavra['make']
print pQQSerSpam, pQQNaoSpam


S = csv.DictWriter(open(folderPath + 'learnedSpam.csv', 'wb'), palavras)
S.writeheader()
S.writerow(pSpamByPalavra)

L = csv.DictWriter(open(folderPath + 'learnedNormal.csv', 'wb'), palavras)
L.writeheader()
L.writerow(pNormalByPalavra)
