import copy

from btree import *
from eightpuzzle import *

from view import *

class metodoBusca(object):

    debug = 0
    def __init__(self,debog=0):
        self.debug = debog

    def gerarOpcoes(self,puzzle):

        chaves = []
        
        auxPuzzle = copy.deepcopy(puzzle)
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
                #retorna uma lista de strings!
        return chaves

    def impResultado(self, moduloUtilizado):

        moduloUtilizado = reversed(moduloUtilizado)

        print("Movimentos")
        count = 0
        for movimento in moduloUtilizado:
            print("| N | ",count)
            movimento.puzzle.printConteudo()
            count = count + 1

        print("FIM")
    
    def amplitude(self,inicio,fim,debug = 0):

        vieww = View()

        arvore = tree(node(inicio))
        last_leaf = node(fim)

        #return None = ruim node = good
        while (arvore.buscarPuzzleReal(arvore.retornaRoot(), last_leaf) == None):   
            vieww.progressBar('Número de Tentativas: ',vieww.addCount(),'Tempo:')
            #tem que add na arvore os novos caminhos
            
            #pega o conteudo das folhas e bota na lista 
            folhas = copy.deepcopy(arvore.irF   olha(arvore.retornaRoot()))

            #Faz o insert de cada folha 
            for x in  range(len(folhas)):
               
                opcoesFolhas = copy.deepcopy(self.gerarOpcoes(folhas[x].puzzle))
                
                arvore.inserir(folhas[x],opcoesFolhas)
                if(self.debug == 1):
                    print ("Folha:", folhas[x].id_puzzle)
            
            if(self.debug == 1):
                print('Next ----------------------------------------------')


        #Mostar Caminho. 
        if(debug == 1):
            print ("Chegou no final!")

        return arvore.mostarCaminho(last_leaf)
    
    def profundidade(self, inicio, fim):
        
        viewww = View()

        arvore = tree(node(inicio))
        last_leaf = node(fim)

        #return None = ruim node = good,

        #enquanto nao acha o node ele.
        aux_atual = node(inicio)
        while (arvore.buscarPuzzleReal(arvore.retornaRoot(), last_leaf) == None):   
            
            if aux_atual != None:
                #verifica se o atual esta na lista
                if (aux_atual.id_puzzle in arvore.inseridos and aux_atual.id_puzzle != arvore.retornaRoot().id_puzzle):
                    print("ESSE NODE JÀ ESTA NA LISTA")
                else:
                    print("add esse node a lista!")

                opcoesFolhas = copy.deepcopy(self.gerarOpcoes(aux_atual.puzzle))
                aux_atual.keys = opcoesFolhas

                filhos_Lista, filhos_opces = 0,0
                # verifica se os filhos do atual esta na lista
                for filhos in aux_atual.keys:
                    if(filhos != None):
                        filhos_opces = filhos_opces + 1
                        filhos.pai = aux_atual
                        if(filhos in arvore.inseridos):
                            filhos_Lista = filhos_Lista + 1
                if filhos_Lista == filhos_opces:
                    #se tiver bota o atual na lista e cancela ele(Volta para o pai)
                    print("ESSEs FILHOS JÀ FOI INSERIDOS")

                    #Add esse node na lista
                    #volta para o pai
                    break
                #se não vai no filho da esquedar, se não tiver o filho de baixo, direita e cima
                if(aux_atual.keys[0] != None):
                    aux_atual = aux_atual.keys[0]
                elif(aux_atual.keys[0] != None):
                    aux_atual = aux_atual.keys[0]
                elif(aux_atual.keys[0] != None):
                    aux_atual = aux_atual.keys[0]
                elif(aux_atual.keys[0] != None):
                    aux_atual = aux_atual.keys[0]
            else:
                aux_atual = aux_atual.pai

        #     #viewww.progressBar('Número de Tentativas: ',vieww.addCount(),'Tempo:')
            
        #     for inseridos in arvore.inseridos:
                
        #         #Primeiro da lista
        #         node_atual = copy.deepcopy(arvore.buscarPuzzleReal(arvore.retornaRoot(),node(inseridos)))

        #         #Se todos os filhos já foram colocados PARA
        #         opcoesFolhas = copy.deepcopy(self.gerarOpcoes(node_atual.puzzle))
                
        #         count_inseridos, countopcoes = 0 , 0
        #         for opcoes in opcoesFolhas:
        #             if(opcoes != None):
        #                 countopcoes = countopcoes + 1
        #                 if(opcoes.id_puzzle in arvore.inseridos):
        #                     print("Já foi inserido")
        #                     count_inseridos = count_inseridos +1
        #             else:
        #                 print("Ta de boas")

        #         if(count_inseridos == countopcoes):
        #             print("todas as opcoes já foram escolhidas.....")

        #         node_aux = node(node_atual)
        #         node_aux.keys = opcoesFolhas
        #         #primeiro testa todas as opcoes de cada lado
                
        #         #enquanto todos os flhos não estão na arvore, testar eles?????
        #         #quando todos os filhos estiverem na arvore, corta essa opção, add ela e  para!

        #         while node_aux.keys[0] != None:
        #             #verfica ele!
        #             node_aux.pai = copy.deepcopy(node_aux)
        #             node_aux = node_aux.keys[0]
        #             ##add opcoes do filho!
        #             opcoesFolhas = copy.deepcopy(self.gerarOpcoes(node_aux.puzzle))
        #             node_aux.keys = opcoesFolhas
                    
        #             #verifica se ja não tem os filhos
        #             for opcoes in opcoesFolhas:
        #             if(opcoes != None):
        #                 countopcoes = countopcoes + 1
        #                 if(opcoes.id_puzzle in arvore.inseridos):
        #                     print("Já foi inserido")
        #                     count_inseridos = count_inseridos +1
        #             else:
        #                 print("Ta de boas")

        #             ##add filho na arvore

        #             ##boa


        #     #verifica se o  filhos já estão na arvore,
        #     while node_atual.keys[0] != None:
        #         #vai para esquerda
        #         opcoesFolhas = copy.deepcopy(self.gerarOpcoes(folhas[x].puzzle))
                

        #     #node 
            
        #     #se não tiver bota eles e verifica os filhos na ordem ( e -> b -> d -> c )



        #     #pega o conteudo das folhas e bota na lista 
        #     folhas = copy.deepcopy(arvore.irFolha(arvore.retornaRoot()))

        #     #Faz o insert de cada folha 
        #     for x in  range(len(folhas)):
               
        #         opcoesFolhas = copy.deepcopy(self.gerarOpcoes(folhas[x].puzzle))
                
        #         arvore.inserir(folhas[x],opcoesFolhas)
        #         if(self.debug == 1):
        #             print ("Folha:", folhas[x].id_puzzle)
            
        #     if(self.debug == 1):
        #         print('Next ----------------------------------------------')


        # #Mostar Caminho. 
        # if(debug == 1):
        #     print ("Chegou no final!")

        # return arvore.mostarCaminho(last_leaf)


        # l1 = lista()
        # l2 = lista()
        # visitado = []
        
        # l1.insereUltimo(inicio,0,None)
        # l2.insereUltimo(inicio,0,None)

        # linha = []
        # linha.append(inicio)
        # linha.append(0)
        # visitado.append(linha)

        # while l1.vazio() is not None:
        #     atual = l1.deletaUltimo()
        #     if atual is None: break
        #     ind = nos.index(atual.valor1)
        #     for i in range(len(grafo[ind])-1,-1,-1):
        #         novo = grafo[ind][i]
        #         flag = True

        #         for j in range(len(visitado)):
        #             if visitado[j][0]==novo:
        #                 if visitado[j][1]<=(atual.valor2+1):
        #                     flag = False
        #                 else:
        #                     visitado[j][1]=atual.valor2+1
        #                 break
                
        #         if flag:
        #             l1.insereUltimo(novo, atual.valor2 + 1 , atual)
        #             l2.insereUltimo(novo, atual.valor2 + 1, atual)
        #             linha = []
        #             linha.append(novo)
        #             linha.append(atual.valor2+1)
        #             visitado.append(linha)
        #             if novo == fim:
        #                 caminho = []
        #                 caminho = l2.exibeCaminho()
        #                 return caminho

        # return "odartnocne oãn ohnimaC"


    def profundidade_limitada(self, inicio, fim):
        pass

    def aprofundamento_iterativo(self, inicio, fim):
        pass

    def bidirecional(self, inicio, fim):
        pass

if __name__ == "__main__":
    
    from eightpuzzle import *

    inicio = eightPuzzle([['X','2','3'],
                        ['1','5','6'], 
                        ['4','7','8']])

    fim    = eightPuzzle([['1','2','3'],
                        ['4','5','6'], 
                        ['7','8','X']])

    sol = metodoBusca()
    # amplitude = sol.amplitude(inicio,fim)

    # amplitude = reversed(amplitude)

    print("Movimentos")
    # inicio.printConteudo()

    sol.profundidade(inicio,fim)

    # for movimento in amplitude:
    #     movimento.puzzle.printConteudo()

    # print("FIM")