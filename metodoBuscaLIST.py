import copy,sys,time

from blista import node, Blista
from eightpuzzle import *

from view import *

class metodoBusca(object):
    debug = 0
    def __init__(self,debog=0):
        self.debug = debog

    def gerarOpcoes(self,node_entrada):

        chaves = []
        
        auxPuzzle = copy.deepcopy(node_entrada.puzzle)
        chaves = auxPuzzle.liberadaOpcoes()

        for x in range(4):
            if chaves[x] == False:
                chaves[x] = None
            else:
                movimento = copy.deepcopy(auxPuzzle)
                if (x == 0):
                    movimento.moverCima()
                elif (x == 1):
                    movimento.moverBaixo()
                elif (x == 2):
                    movimento.moverDireita()
                elif (x == 3):
                    movimento.moverEsquerda()
                else:
                    exit('ERRRRRO')

                chaves[x] = node(eightPuzzle(movimento.getConteudo()))
                chaves[x].pai = node_entrada
                #retorna uma lista de strings!
        return chaves


    def amplitude(self,inicio,fim):
        tic = time.perf_counter()
        #vieww = View()
        print('Iniciando amplitude()')
        listona = Blista()
        listona.insertHead(node(inicio))
        if(self.debug == 1):    
            print ("Folha add e filhos:", listona.readHead().id_puzzle)
            print('Next ----------------------------------------------')

        last_leaf = node(fim)

        #return None = ruim node = good
        #Enquanto não tem na lista cintinua
        while (listona.readNode(last_leaf) == None):   
            #vieww.progressBar('Número de Tentativas: ',vieww.addCount(),'Tempo:')
            #tem que add na arvore os novos caminhos
            
            #pega o conteudo das folhas e bota na lista 
            folhas = listona.readLeaf()

            #Faz o insert de cada folha 
            for x in  range(len(folhas)):
                if(self.debug == 1):
                    print("Tranalhando com a folha: ",x)

                opcoesFolhas = self.gerarOpcoes(folhas[x])
                
                folhas[x].keys = opcoesFolhas 

                #update da folha
                listona.updateNode(folhas[x])

                ##inserir os filhos
                for opcoes in opcoesFolhas:
                    if(opcoes != None):
                        listona.insertTail(opcoes,self.debug) 
                        if(opcoes.id_puzzle == last_leaf.id_puzzle):
                            if(self.debug == 1):
                                print("VALOR ENCONTRADO!")

                        if(self.debug == 1):
                            print ("Folha add e filhos:", opcoes.id_puzzle)
                        
            if(self.debug == 1):
                print('Next ----------------------------------------------')


        #Mostar Caminho. 
        if(self.debug == 1):
            print ("Chegou no final!")

        #timer!!!
        amplitude_result={
            'TEMPO_AMPLITUDADE':    time.perf_counter() - tic,
            'N_NODE_AMPLITUDE' :    listona.total_nodes,
            'E_MEMORIA':sys.getsizeof(listona),
            'MOVIMENTOS_AMPLITUDE':list(reversed(listona.readNode(last_leaf))),
            'N_MOVIMENTOS': 0,
            'tipo':0
        }
        amplitude_result['N_MOVIMENTOS'] = len(amplitude_result['MOVIMENTOS_AMPLITUDE'])
        return amplitude_result

    def profundidade(self,inicio,fim):
        tic = time.perf_counter()
        print ("Iniciando profundidade()")

        last_leaf = node(fim)

        boardVisited = Blista()
        stack = list([node(inicio)])
        
        while stack:
            if(self.debug == 2):
                print("Stank bem grande", len(stack))

            node_atual = stack.pop()
            if(self.debug == 1):
                print("Tranalhando com a folha: ",node_atual.id_puzzle)
            boardVisited.insertTail(node_atual)

            if node_atual.id_puzzle == last_leaf.id_puzzle:
                print("ACHOU!!!!!!!!!!!!")
                last_leaf=node_atual
                boardVisited.updateNode(last_leaf)
                break
            #Inverse the order of next paths for execution porpuses

            #Opcoes
            opcoesFolhas = self.gerarOpcoes(node_atual)

            #Arrumar aqui!!!!!
            for path in opcoesFolhas:
                if (path != None and boardVisited.readNode(path) == None):
                    stack.append(path)
                    # boardVisited.insertTail(path)
                    if(self.debug == 1):
                            print ("Folha add e filhos:", path.id_puzzle)
                elif(path != None ):
                    if(self.debug == 1):
                        print ("Folha já foi add:")  

            
            if(self.debug == 1):
                print('Next ----------------------------------------------')
        #Mostar Caminho. 
        if(self.debug == 1):
            print ("Chegou no final!")

        saida = reversed(boardVisited.readNode(last_leaf))
        
        profundidade_result ={
            'TEMPO_PROFUNDIDADE':time.perf_counter() - tic,
            'N_NODE_PROFUNDIDADE': boardVisited.total_nodes,
            'E_MEMORIA_PROFUNDIDADE':sys.getsizeof(boardVisited),
            'N_MOVIMENTOS_PROFUNDIDADE':0,
            'MOVIMENTOS_PROFUNDIDADE':list(saida),
            'tipo':1
        }

        if(saida == None):
            return ["Caminho não encontrado"]
        else:
            profundidade_result['N_MOVIMENTOS_PROFUNDIDADE'] = len(profundidade_result['MOVIMENTOS_PROFUNDIDADE'])
            return profundidade_result

    def profundidade_limitada(self,inicio,fim,limite):
        tic = time.perf_counter()
        print("iniciando profundidade_limitada")
        last_leaf = node(fim)

        boardVisited = Blista()
        stack = list([node(inicio)])
        
        while stack:
            
            node_atual = stack.pop()
            if(self.debug == 1):
                print("Trabalhando com a folha: ",node_atual.id_puzzle)
            boardVisited.insertTail(node_atual)

            #Verifica se é o node atual!
            if node_atual.id_puzzle == last_leaf.id_puzzle:
                print("ACHOU!!!!!!!!!!!!")
                last_leaf=node_atual
                boardVisited.updateNode(last_leaf)
                break
            #Inverse the order of next paths for execution porpuses
            if( len(boardVisited.readNode(node_atual)) > limite):
                return ["erro","Limite max"]

            #Opcoes
            opcoesFolhas = self.gerarOpcoes(node_atual)

            #implementa os filhos
            for path in opcoesFolhas:
                if (path != None and boardVisited.readNode(path) == None):
                    stack.append(path)
                    # boardVisited.insertTail(path)
                    if(self.debug == 1):
                            print ("Folha add e filhos:", path.id_puzzle)
                elif(path != None ):
                    if(self.debug == 1):
                        print ("Folha já foi add:")  

            
            if(self.debug == 1):
                print('Next ----------------------------------------------')
        #Mostar Caminho. 
        if(self.debug == 1):
            print ("Chegou no final!")

        profundidade_limitada_result = {
            'TEMPO_PROFUNDIDADE_LIMITADA':time.perf_counter() - tic,
            'N_NODE_PROFUNDIDADE_LIMITADA':boardVisited.total_nodes,
            'N_MOVIMENTOS_PROFUNDIDADE_LIMITADA':0,
            'E_MEMORIA_PROFUNDIDADE':sys.getsizeof(boardVisited),
            'Limite_PROFUNDIDADE_LIMITADA':1000,
            'MOVIMENTOS_PROFUNDIDADE_LIMITADA' : list(reversed(boardVisited.readNode(last_leaf))),
            'tipo':2
        }

        if(boardVisited.readNode(last_leaf) == None):
            return ["Caminho não encontrado"]
        else:
            profundidade_limitada_result['N_MOVIMENTOS_PROFUNDIDADE_LIMITADA']= len(profundidade_limitada_result['MOVIMENTOS_PROFUNDIDADE_LIMITADA'])
            return profundidade_limitada_result 

    def aprofundamento_iterativo(self,inicio,fim, l_max):
        tic = time.perf_counter()
        print("Começando aprofundamento_iterativo()")
        last_leaf = node(fim)

        boardVisited = Blista()
        boardVisited.insertHead(node(inicio))

        for limite in range(1,l_max+1):
            stack = list(boardVisited.readLeaf())
            if(self.debug == 1):
                print("Limite:",limite," de ",l_max+1)

            while stack != []:

                #verifica se já foi encontrado
                # profundidade = boardVisited.readNode(last_leaf)
                # if(profundidade != None):
                #     if(self.debug == 1):
                #         print("Node encontrado!")
                #     return profundidade



                node_atual = stack.pop()
                if(self.debug == 1):
                    print("Tranalhando com a folha: ",node_atual.id_puzzle)


                #verifica a profundidade
                if(len(boardVisited.readNode(node_atual)) > limite):
                    if(self.debug == 1):
                        print("Profunidade Atingiu o limite")
                    break
                    return ["Erro","Limite Max"]

                #verifica se o node_atual é igual ao objetivo
                if(node_atual.id_puzzle == last_leaf.id_puzzle):
                    print("Node encontrada")
                    last_leaf = node_atual
                    boardVisited.updateNode(last_leaf)
                    # return last_leaf

                    saida = reversed(boardVisited.readNode(last_leaf))
                    aprofudamento_iterativo_result ={
                        'TEMPO_APROFUNDAMENTO':time.perf_counter() -tic,
                        'N_NODE_APROFUNDAMENTO':boardVisited.total_nodes,
                        'N_MOVIMENTOS_APROFUNDAMENTO':0,
                        'E_MEMORIA_APROFUNDAMENTO':sys.getsizeof(boardVisited),
                        'LIMITE_MAXIMO_PROFUNDIDADE':1100,
                        'MOVIMENTOS_APROFUNDAMENTOE':list(saida),
                        'tipo':3
                    }
                    aprofudamento_iterativo_result['N_MOVIMENTOS_APROFUNDAMENTO'] = len(aprofudamento_iterativo_result['MOVIMENTOS_APROFUNDAMENTOE'])
                    return aprofudamento_iterativo_result
                    break
    
                #Pesquisa os filhos!
                opcoesFolhas = self.gerarOpcoes(node_atual)

                node_atual.keys = opcoesFolhas
                boardVisited.insertTail(node_atual)

                #implementa os filhos
                for path in opcoesFolhas:
                    if (path != None and boardVisited.readNode(path) == None):
                        # stack.append(path)
                        boardVisited.insertTail(path)
                        if(self.debug == 1):
                                print ("Folha add e filhos:", path.id_puzzle)
                    elif(path != None ):
                        if(self.debug == 1):
                            print ("Folha já foi add:")  
                #Atualiza o node
                


                if(self.debug == 1):
                    print('Next ----------------------------------------------')

        saida = reversed(boardVisited.readNode(last_leaf))
        aprofudamento_iterativo_result ={
            'TEMPO_APROFUNDAMENTO':time.perf_counter() -tic,
            'N_NODE_APROFUNDAMENTO':boardVisited.total_nodes,
            'N_MOVIMENTOS_APROFUNDAMENTO':0,
            'E_MEMORIA_APROFUNDAMENTO':sys.getsizeof(boardVisited),
            'LIMITE_MAXIMO_PROFUNDIDADE':1100,
            'MOVIMENTOS_APROFUNDAMENTOE':list(saida),
            'tipo':3
        }

        if(saida == None):
            return ["Erro","Caminho não encontrado"]
        else:
            aprofudamento_iterativo_result['N_MOVIMENTOS_APROFUNDAMENTO'] = len(aprofudamento_iterativo_result['MOVIMENTOS_APROFUNDAMENTOE'])
            return aprofudamento_iterativo_result

    def bidirecional(self,inicio,fim):
        tic = time.perf_counter()
        print("Começando Bidirecional()")
        listaInicio = Blista()
        listaFim = Blista()

        listaInicio.insertHead(node(inicio))
        listaFim.insertHead(node(fim))

        listaSaida = Blista()
        saida = True
        while saida:

            #Primeira Lista
            #Pega o conteudo das folhas e bota na lista
            folhas_l1 = listaInicio.readLeaf()
            folhas_l2 = listaFim.readLeaf()

            #Verificar se um existe no outro (folhas com folhas)
            for folhas_l in folhas_l1:
                node_fim = listaFim.readNode(folhas_l)
                if(node_fim != None):
                    #verifica qual filho (movimento) e o da esquerda e liga o resto dos pontos na impressao
                    nota_atual = folhas_l
                    opcoesFolhas = self.gerarOpcoes(nota_atual)

                    for opcoes in opcoesFolhas:
                        for nodenofim in node_fim:
                            if(opcoes != None and opcoes.id_puzzle == nodenofim.id_puzzle):
                                if(self.debug == 1):
                                    print("Localizado!")

                                for pais in list(reversed(listaInicio.readNode(nota_atual))):   
                                    pais.proximo = None
                                    pais.anterior = None 
                                    listaSaida.insertTail(pais)
                                
                                for pais_fim in node_fim:
                                    pais_fim.proximo = None
                                    pais_fim.anterior = None 
                                    listaSaida.insertTail(pais_fim)
                                
                                bidirecional = {
                                    'TEMPO_BIDIRECIONAL':time.perf_counter() - tic,
                                    'N_NODE_BIDIRECIONAL':listaFim.total_nodes + listaInicio.total_nodes,
                                    'N_MOVIMENTOS_BIDIRECIONAL':0,
                                    'E_MEMORIA_BIDIRECIONAL':sys.getsizeof(listaInicio)+sys.getsizeof(listaFim)+sys.getsizeof(listaSaida),
                                    'MOVIMENTOS_BIDIRECIONAL':listaSaida.readAll(),
                                    'tipo':4
                                }

                                bidirecional['N_MOVIMENTOS_BIDIRECIONAL'] = len(bidirecional['MOVIMENTOS_BIDIRECIONAL'])
                                return bidirecional

            #lista de inicio
            for folha in range(len(folhas_l1)):
                if(self.debug == 1):
                    print("Tranalhando com a folha (Lista 1): ",folhas_l1[folha].id_puzzle)

                opcoesFolhas = self.gerarOpcoes(folhas_l1[folha])

                #associar as folhas
                folhas_l1[folha].keys = opcoesFolhas 

                #update da folha
                listaInicio.updateNode(folhas_l1[folha])

                for opcoes in opcoesFolhas:
                    if(opcoes != None):
                        listaInicio.insertTail(opcoes,self.debug) 

                        if(self.debug == 1):
                            print ("Folha add e filhos:", opcoes.id_puzzle)

            #lista de fim
            for folha in range(len(folhas_l2)):
                if(self.debug == 1):
                    print("Tranalhando com a folha (Lista 2): ",folhas_l2[folha].id_puzzle)

                opcoesFolhas = self.gerarOpcoes(folhas_l2[folha])

                #associar as folhas
                folhas_l2[folha].keys = opcoesFolhas 

                #update da folha
                listaFim.updateNode(folhas_l2[folha])

                for opcoes in opcoesFolhas:
                    if(opcoes != None):
                        listaFim.insertTail(opcoes,self.debug) 

                        if(self.debug == 1):
                            print ("Folha add e filhos:", opcoes.id_puzzle)

if __name__ == "__main__":
    
    from eightpuzzle import *

    inicio = eightPuzzle([['X','2','3'],
                          ['1','5','6'], 
                          ['4','7','8']])

    # inicio = eightPuzzle([['1','2','3'],['4','8','5'],['7','X','6']])

    fim    = eightPuzzle([['1','2','3'],
                          ['4','5','6'], 
                          ['7','8','X']])

    sol = metodoBusca()


    print("Profundidade")
    dic_profu = sol.profundidade(inicio, fim)
    print('-'*50)
    print("Profundidade Limitada")
    dic_profu_limita = sol.profundidade_limitada(inicio, fim,10*4)
    print('-'*50)
    print("Profundidade")
    dic_aprofudamento = sol.aprofundamento_iterativo(inicio, fim,5)
    print('-'*50)
    print("Profundidade")
    dic_bidirecional = sol.bidirecional(inicio, fim)
    print('-'*50)
    print("Amplitude")
    dic_amplitude = sol.amplitude(inicio,fim)      
    print('-'*50)
    print("FIM")