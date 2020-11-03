import time

class View(object):
    #Futaramente usar o tkinter
    count = 0
    __lastTime = 0
    __newTime = 0
    __totalTime = 0

    timepass = 0

    def addCount(self, valor =1, __newTime = 0):
        self.count = self.count +1
        
        self.__totalTime = self.__totalTime + self.timepass

        self.timepass = abs(self.__lastTime - self.__newTime)

        self.__lastTime = self.__newTime

        return self.count

    def progressBar(self, title, total,title2= '',time2 = ''):
        #Atualizacao do tempo
        self.__newTime = time.time()

        if(title2 != ""):
            time2 = str(self.timepass)
        
        print(title,'%s' % (total) ,title2, '%s' % (time2), end='\r')
    # print("")

    def __init__(self):
        self.__lastTime = time.time()

    def setBarra(self):
        pass

    def addBarra(self):
        pass

    def endBarra(self):
        pass

import os
class montarView(object):
    lista=[0,0,0,0,0,0,0,0]

    saidaFile = open('view/view.html','r+',encoding='utf-8').read()

    def __init__(self,inicio = '',fim =''):
        if(inicio != ''):
            self.saidaFile = open('view/view.html','r+',encoding='utf-8').read()
            
            self.saidaFile = self.saidaFile.replace('%%NODE_INICIO%%',self.prepararMovimento(str(inicio)))
            self.saidaFile = self.saidaFile.replace('%%NODE_FIM%%',self.prepararMovimento(str(fim)))

    def showResults(self):
        os.system("start saida.html")

    def salvarArquivo(self):
        saida = open('saida.html','w+', encoding='utf-8')
        
        saida.write(self.saidaFile)

        saida.close()

    def atualizarResultado(self,dicionario, default = 0):
        if(default == 1):
            os.system("rm saida.html")

        if(dicionario['tipo'] == 0):
            #amplitude
            self.saidaFile = self.saidaFile.replace('%%TEMPO_AMPLITUDADE%%',str(dicionario['TEMPO_AMPLITUDADE']))
            self.saidaFile = self.saidaFile.replace('%%N_NODE_AMPLITUDE%%',str(dicionario['N_NODE_AMPLITUDE']))
            self.saidaFile = self.saidaFile.replace('%%N_MOVIMENTOS%%',str(dicionario['N_MOVIMENTOS']))
            self.saidaFile = self.saidaFile.replace('%%E_MEMORIA%%',str(dicionario['E_MEMORIA']))
            
            movimentos = ""

            if(dicionario['MOVIMENTOS_AMPLITUDE'] != []):
                for x in dicionario['MOVIMENTOS_AMPLITUDE']:
                    movimentos = movimentos + self.prepararMovimento(x.id_puzzle)
            self.saidaFile = self.saidaFile.replace('%%MOVIMENTOS_AMPLITUDE%%',movimentos)
            
            self.lista[0] = 1        
       
        elif(dicionario['tipo'] == 1):
            #profundidade
            self.saidaFile = self.saidaFile.replace('%%TEMPO_PROFUNDIDADE%%',str(dicionario['TEMPO_PROFUNDIDADE']))
            self.saidaFile = self.saidaFile.replace('%%N_NODE_PROFUNDIDADE%%',str(dicionario['N_NODE_PROFUNDIDADE']))
            self.saidaFile = self.saidaFile.replace('%%N_MOVIMENTOS_PROFUNDIDADE%%',str(dicionario['N_MOVIMENTOS_PROFUNDIDADE']))
            self.saidaFile = self.saidaFile.replace('%%E_MEMORIA_PROFUNDIDADE%%',str(dicionario['E_MEMORIA_PROFUNDIDADE']))
            
            movimentos = ""

            if(dicionario['MOVIMENTOS_PROFUNDIDADE'] != []):
                for x in dicionario['MOVIMENTOS_PROFUNDIDADE']:
                    movimentos = movimentos + self.prepararMovimento(x.id_puzzle)
            self.saidaFile = self.saidaFile.replace('%%MOVIMENTOS_PROFUNDIDADE%%',movimentos)
            
            self.lista[1] = 1  
        elif(dicionario['tipo'] == 2):
            #profundidade limitada
            self.saidaFile = self.saidaFile.replace('%%TEMPO_PROFUNDIDADE_LIMITADA%%',str(dicionario['TEMPO_PROFUNDIDADE_LIMITADA']))
            self.saidaFile = self.saidaFile.replace('%%N_NODE_PROFUNDIDADE_LIMITADA%%',str(dicionario['N_NODE_PROFUNDIDADE_LIMITADA']))
            self.saidaFile = self.saidaFile.replace('%%N_MOVIMENTOS_PROFUNDIDADE_LIMITADA%%',str(dicionario['N_MOVIMENTOS_PROFUNDIDADE_LIMITADA']))
            self.saidaFile = self.saidaFile.replace('%%E_MEMORIA_PROFUNDIDADE%%',str(dicionario['E_MEMORIA_PROFUNDIDADE']))
            self.saidaFile = self.saidaFile.replace('%%Limite_PROFUNDIDADE_LIMITADA%%',str(dicionario['Limite_PROFUNDIDADE_LIMITADA']))
            
            movimentos = ""

            if(dicionario['MOVIMENTOS_PROFUNDIDADE_LIMITADA'] != []):
                for x in dicionario['MOVIMENTOS_PROFUNDIDADE_LIMITADA']:
                    movimentos = movimentos + self.prepararMovimento(x.id_puzzle)
            self.saidaFile = self.saidaFile.replace('%%MOVIMENTOS_PROFUNDIDADE_LIMITADA%%',movimentos)
            
            self.lista[2] = 1  
        elif(dicionario['tipo'] == 3):
            #Aprofudamento iteratico
            self.saidaFile = self.saidaFile.replace('%%TEMPO_APROFUNDAMENTO%%',str(dicionario['TEMPO_APROFUNDAMENTO']))
            self.saidaFile = self.saidaFile.replace('%%N_NODE_APROFUNDAMENTO%%',str(dicionario['N_NODE_APROFUNDAMENTO']))
            self.saidaFile = self.saidaFile.replace('%%N_MOVIMENTOS_APROFUNDAMENTO%%',str(dicionario['N_MOVIMENTOS_APROFUNDAMENTO']))
            self.saidaFile = self.saidaFile.replace('%%E_MEMORIA_APROFUNDAMENTO%%',str(dicionario['E_MEMORIA_APROFUNDAMENTO']))
            self.saidaFile = self.saidaFile.replace('%%LIMITE_MAXIMO_PROFUNDIDADE%%',str(dicionario['LIMITE_MAXIMO_PROFUNDIDADE']))
            
            movimentos = ""

            if(dicionario['MOVIMENTOS_APROFUNDAMENTOE'] != []):
                for x in dicionario['MOVIMENTOS_APROFUNDAMENTOE']:
                    movimentos = movimentos + self.prepararMovimento(x.id_puzzle)
            self.saidaFile = self.saidaFile.replace('%%MOVIMENTOS_APROFUNDAMENTOE%%',movimentos)
            
            self.lista[3] = 1  
        elif(dicionario['tipo'] == 4):
             #Aprofudamento iteratico
            self.saidaFile = self.saidaFile.replace('%%TEMPO_BIDIRECIONAL%%',str(dicionario['TEMPO_BIDIRECIONAL']))
            self.saidaFile = self.saidaFile.replace('%%N_NODE_BIDIRECIONAL%%',str(dicionario['N_NODE_BIDIRECIONAL']))
            self.saidaFile = self.saidaFile.replace('%%N_MOVIMENTOS_BIDIRECIONAL%%',str(dicionario['N_MOVIMENTOS_BIDIRECIONAL']))
            self.saidaFile = self.saidaFile.replace('%%E_MEMORIA_BIDIRECIONAL%%',str(dicionario['E_MEMORIA_BIDIRECIONAL']))
            
            movimentos = ""

            if(dicionario['MOVIMENTOS_BIDIRECIONAL'] != []):
                for x in dicionario['MOVIMENTOS_BIDIRECIONAL']:
                    movimentos = movimentos + self.prepararMovimento(x.id_puzzle)
            self.saidaFile = self.saidaFile.replace('%%MOVIMENTOS_BIDIRECIONAL%%',movimentos)
            
            self.lista[4] = 1 
        elif(dicionario['tipo'] == 5):
            #Custo uniforme
            self.saidaFile = self.saidaFile.replace('%%TEMPO_CUSTOUNIFORME%%',str(dicionario['TEMPO']))
            self.saidaFile = self.saidaFile.replace('%%N_NODE_CUSTOUNIFORME%%',str(dicionario['N_NODE']))
            self.saidaFile = self.saidaFile.replace('%%N_MOVIMENTOS_CUSTOUNIFORME%%',str(dicionario['N_MOVIMENTOS']))
            self.saidaFile = self.saidaFile.replace('%%E_MEMORIA_CUSTOUNIFORME%%',str(dicionario['E_MEMORIA']))
            
            movimentos = ""

            if(dicionario['MOVIMENTOS'] != []):
                for x in dicionario['MOVIMENTOS']:
                    movimentos = movimentos + self.prepararMovimento(x.id_puzzle)
            self.saidaFile = self.saidaFile.replace('%%MOVIMENTOS_CUSTOUNIFORME%%',movimentos)
            
            self.lista[5] = 1 
        elif(dicionario['tipo'] == 6):
            #Greedy
            self.saidaFile = self.saidaFile.replace('%%TEMPO_GREEDY%%',str(dicionario['TEMPO']))
            self.saidaFile = self.saidaFile.replace('%%N_NODE_GREEDY%%',str(dicionario['N_NODE']))
            self.saidaFile = self.saidaFile.replace('%%N_MOVIMENTOS_GREEDY%%',str(dicionario['N_MOVIMENTOS']))
            self.saidaFile = self.saidaFile.replace('%%E_MEMORIA_GREEDY%%',str(dicionario['E_MEMORIA']))
            
            movimentos = ""

            if(dicionario['MOVIMENTOS'] != []):
                for x in dicionario['MOVIMENTOS']:
                    movimentos = movimentos + self.prepararMovimento(x.id_puzzle)
            self.saidaFile = self.saidaFile.replace('%%MOVIMENTOS_GREEDY%%',movimentos)
            
            self.lista[6] = 1

        elif(dicionario['tipo'] == 7):
            #Aestrela
            self.saidaFile = self.saidaFile.replace('%%TEMPO_AESTRELA%%',str(dicionario['TEMPO']))
            self.saidaFile = self.saidaFile.replace('%%N_NODE_AESTRELA%%',str(dicionario['N_NODE']))
            self.saidaFile = self.saidaFile.replace('%%N_MOVIMENTOS_AESTRELA%%',str(dicionario['N_MOVIMENTOS']))
            self.saidaFile = self.saidaFile.replace('%%E_MEMORIA_AESTRELA%%',str(dicionario['E_MEMORIA']))
            
            movimentos = ""

            if(dicionario['MOVIMENTOS'] != []):
                for x in dicionario['MOVIMENTOS']:
                    movimentos = movimentos + self.prepararMovimento(x.id_puzzle)
            self.saidaFile = self.saidaFile.replace('%%MOVIMENTOS_AESTRELA%%',movimentos)
            
            self.lista[7] = 1 
    def prepararMovimento(self,movimento=list):
        '''
            Faz um movimento de cada vez, retornar um string com o formato html
        '''
        modelo = open("view/moves.html",'r+')

        saida = modelo.read()
        puzzle = list(movimento)
        for x in range(9):
            if(puzzle[x].upper() == 'X'):
                saida = saida.replace('>%'+str(x+1)," style='background:aquamarine;' >"+puzzle[x])
            else:
                saida = saida.replace('%'+str(x+1),puzzle[x])

        
        return saida

if __name__ == "__main__":
    import sys 

    htmlview = montarView()
    amplitude_result={
    'TEMPO_AMPLITUDADE':00.00,
    'N_NODE_AMPLITUDE' : 0,
    'N_MOVIMENTOS':0,
    'E_MEMORIA':0,
    'MOVIMENTOS_AMPLITUDE':[],
    'tipo':0
    }
    htmlview.atualizarResultado(amplitude_result)
    # htmlview.salvarArquivo()
    # htmlview.showResults()
     
    # Any Integer Value
    print(sys.getsizeof(htmlview)) 

    # movimeneto = '12345678x'
    # print(htmlview.prepararMovimento(movimeneto))