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
k = int(input("informe o valor de K: "))
acuracia = 0

def lerBase(baseV, baseT):

    arquivoV = open('baseV.txt', 'r')
    
    arquivoT = open('baseT.txt','r')
    
    #lê o arquivo de validação
    for linha in arquivoV:
        dado = None
        dado = linha.split()
        lim = Limao(float(dado[0]), float(dado[1]), float(dado[2]), str(dado[3]))
        baseV.append(lim)
    arquivoV.close()
    
    #lê o arquivo de teste
    for linha in arquivoT:
        dado = None
        dado = linha.split()
        lim = Limao(float(dado[0]), float(dado[1]), float(dado[2]), str(dado[3]))
        baseT.append(lim)
    arquivoT.close()
    
    
    
def calcDistancia(l1, l2):

    return np.sqrt(np.power((l1.getAltura()  - l2.getAltura()),  2) +
                   np.power((l1.getLargura() - l2.getLargura()), 2) +
                   np.power((l1.getPeso()    - l2.getPeso()),    2))
    



baseV = []
baseT = []
lerBase(baseV, baseT)



for i in range(len(baseT)):
   
    cravo  = 0
    galego = 0
    thaiti = 0
    mirin  = 0
    
    for j in range(len(baseV)):
        baseV[j].setDistEq(calcDistancia(baseT[i], baseV[j]))
        
    baseV = sorted(baseV, key=lambda x: x.getDistEq())
    
    for j in range(k):
        classe = baseV[j].getClasse()
        
        if(classe == 'Cravo' ):
            cravo += 1
        elif(classe == 'Galego'):
            galego += 1
        elif(classe == 'Thaiti'):
            thaiti += 1
        else:
            mirin += 1
    
    
    if(cravo > galego and cravo > thaiti and cravo > mirin):
        if(baseT[i].getClasse() == 'Cravo'):
            acertou += 1
        else:
            errou += 1
        
    elif(galego > thaiti and galego > mirin):
        if(baseT[i].getClasse() == 'Galego'):
            acertou += 1
        else:
            errou += 1
        
    elif(thaiti > mirin):
        if(baseT[i].getClasse() == 'Thaiti'):
            acertou += 1
        else:
            errou += 1
    else:
        if(baseT[i].getClasse() == 'Mirin'):
            acertou += 1
        else:
            errou += 1


acuracia = (acertou*100/len(baseT))


print('Acertos: ' + str(acertou))
print("Errou: " + str(errou))
print('acuracia: ' + str(acuracia) + ' %')