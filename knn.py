import numpy as np
import random

class Limao:
    distEq = None

    def __init__(self, altura, largura, peso, classe):
        self.altura = altura
        self.largura = largura
        self.peso = peso
        self.classe = classe

    def setAltura(self, altura):
        self.altura = altura

    def setLargura(self, largura):
        self.largura = largura

    def setPeso(self, peso):
        self.peso = peso

    def setClasse(self, classe):
        self.classe = classe

    def setDistEq(self, dist):
        self.distEq = dist

    def getAltura(self):
        return self.altura

    def getLargura(self):
        return self.largura

    def getPeso(self):
        return self.peso

    def getClasse(self):
        return self.classe

    def getDistEq(self):
        return self.distEq

    def __str__(self):
        return self.classe

errou = 0
acertou = 0
k = 3


def lerBase(base):

    arquivo = open('base.txt', 'r')
    for linha in arquivo:
        dado = None
        dado = linha.split()
        lim = Limao(float(dado[0]), float(dado[1]), float(dado[2]), str(dado[3]))
        base.append(lim)
    arquivo.close()


def calcDistancia(l1, l2):

    return np.sqrt(np.power((l1.getAltura()  - l2.getAltura()),  2) +
                   np.power((l1.getLargura() - l2.getLargura()), 2) +
                   np.power((l1.getPeso()    - l2.getPeso()),    2))
    



base = []
lerBase(base)
random.shuffle(base)



tmBase = len(base)
tmVali = int(len(base)*0.8)
vali = []
tmTest = int(len(base)*0.2)
test = []

for i in range(tmVali):
    vali.append(base[i])

for i in range(tmVali, tmBase):
    test.append(base[i])
    
    cravo  = 0
    galego = 0
    thaiti = 0
    mirin  = 0
    
    for j in range(tmVali):
        vali[j].setDistEq(calcDistancia(base[i], vali[j]))
        
    vali = sorted(vali, key=lambda x: x.getDistEq())
    
    for j in range(k):
        classe = vali[j].getClasse()
        
        if(classe == 'Cravo' ):
            cravo += 1
        elif(classe == 'Galego'):
            galego += 1
        elif(classe == 'Thaiti'):
            thaiti += 1
        else:
            mirin += 1
    
    

    
    
    
    if(cravo > galego and cravo > thaiti and cravo > mirin):
        if(base[i].getClasse() == 'Cravo'):
            acertou += 1
        else:
            errou += 1
        
    elif(galego > thaiti and galego > mirin):
        if(base[i].getClasse() == 'Galego'):
            acertou += 1
        else:
            errou += 1
        
    elif(thaiti > mirin):
        if(base[i].getClasse() == 'Thaiti'):
            acertou += 1
        else:
            errou += 1
    else:
        if(base[i].getClasse() == 'Mirin'):
            acertou += 1
        else:
            errou += 1


print('Acertos: ' + str(acertou))
print("Errou: "+ str(errou))