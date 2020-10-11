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
            folhas = copy.deepcopy(arvore.irFolha(arvore.retornaRoot()))

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
        pass

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
    amplitude = sol.amplitude(inicio,fim)

    amplitude = reversed(amplitude)

    print("Movimentos")
    # inicio.printConteudo()

    for movimento in amplitude:
        movimento.puzzle.printConteudo()

    print("FIM")