import copy
class node(object):
    def __init__(self, puzzle=None, keys = [None,None,None,None]):
        self.pai = None

        self.puzzle    = puzzle
        self.id_puzzle = str(puzzle)

        #Opcoes       #C   B    D    E  
        self.keys = keys

class tree(object):
    __root = None
    inseridos = []
    
    def __init__ (self,puzzle):
        if(puzzle != None):
            self.insereRoot(puzzle)
    
    def retornaRoot(self):
        return self.__root   

    def insereRoot(self, puzzle):
        self.__root = puzzle
        if puzzle.id_puzzle not in self.inseridos:
            self.inseridos.append(puzzle.id_puzzle)

    def irFolha(self,node):
        #Arrumar - Problemas em chegar nas raizes....

        if (len(self.inseridos) == 1):
            #So tem a raiz, logo ela é a unica folha
            return [self.retornaRoot()]
        else:
            saida = []
            for x in self.inseridos:
                nodde = copy.deepcopy(node)
                nodde.id_puzzle = x

                busca = self.buscarPuzzleReal(self.retornaRoot(),nodde)
                if (busca.keys == [None,None,None,None]):
                    saida.append(copy.deepcopy(busca))
            
            return saida

    def buscarPuzzle(self,node_atual,node_buscado):
        for movimento in range(4):
            busca = copy.deepcopy(node_atual)

            while busca != None: 
                if(busca.id_puzzle != node_buscado.id_puzzle):
                    busca = busca.keys[movimento]
                else:
                    return busca

        return None

    def buscarRoot(self,node_atual = node()):
        if node_atual.pai == None:
            return node_atual
        else:
            return self.buscarRoot(node_atual.pai)

    def buscarPuzzleReal(self,node_atual,node_buscado):
        # print(node_atual.id_puzzle.upper(),"\\",node_buscado.id_puzzle.upper())
        #Puxa a raiz aqui, duplica ela com deep copy avanca tudo?
        
        # print("Buscando",node_atual.id_puzzle.upper())

        aux = None

        if (node_atual.id_puzzle.upper() == node_buscado.id_puzzle.upper()):
            return node_atual
        else:
            if (node_atual.keys[0] != None and aux == None):
                aux = self.buscarPuzzleReal(node_atual.keys[0], node_buscado)
            if (node_atual.keys[1] != None and aux == None):
                aux = self.buscarPuzzleReal(node_atual.keys[1], node_buscado)
            if (node_atual.keys[2] != None and aux == None):
                aux = self.buscarPuzzleReal(node_atual.keys[2], node_buscado)
            if (node_atual.keys[3] != None and aux == None):
                aux = self.buscarPuzzleReal(node_atual.keys[3], node_buscado)

        return aux

    def inserir(self,node_atual, keys_valor):
        """
        Node que vai receber os valores
        valores que serao alocados
        """
        if self.retornaRoot() is None:
            #Se não tiver raiz, o node é inserido
            node_atual.keys = keys_valor
            self.__root = node_atual
            
        else:
            for key in range(4):
                if (keys_valor[key] != None and keys_valor[key].id_puzzle in self.inseridos):
                    keys_valor[key] = None

            aux = copy.deepcopy(self.buscarPuzzleReal(self.retornaRoot(),node_atual))

            for chave in range(4):
                if (keys_valor[chave] != None):
                    keys_valor[chave].pai = aux

                    ##inserir chaves
                    if(keys_valor[chave].id_puzzle not in self.inseridos):
                        self.inseridos.append(keys_valor[chave].id_puzzle)    

            if (node_atual.id_puzzle not in self.inseridos):
                self.inseridos.append(node_atual.id_puzzle)

            aux.keys = keys_valor

            self.insereRoot(self.buscarRoot(aux))

    def mostarCaminho(self, node_final):
        #Retonar o caminho de volta dos nodes até a raiz.
        saida = []
        node_final = self.buscarPuzzleReal(self.retornaRoot(),node_final)

        while node_final.pai is not None:
            saida.append(node_final)
            node_final = node_final.pai

        saida.append(self.retornaRoot())
        return saida
#Testes
if __name__ == "__main__":
    from eightpuzzle import *

    no1 = node(eightPuzzle([['X','2','3'],
                            ['1','5','6'], 
                            ['4','7','8']]))
                        #   raiz

    no2 = node(eightPuzzle([['1','2','3'],
                            ['x','5','6'], 
                            ['4','7','8']]))
    no3 = node(eightPuzzle([['2','X','3'],
                            ['1','5','6'], 
                            ['4','7','8']]))
                        # nivel 4

    no4 = node(eightPuzzle([['1','2','3'],
                            ['4','5','6'], 
                            ['X','7','8']]))

    no5 = node(eightPuzzle([['1','2','3'],
                            ['5','X','6'], 
                            ['4','7','8']]))

    no6 = node(eightPuzzle([['2','5','3'],
                            ['1','X','6'], 
                            ['4','7','8']]))

    no7 = node(eightPuzzle([['2','3','X'],
                            ['1','5','6'], 
                            ['4','7','8']])) 
                        #nivel 3        
                                    
    teste_arvore = tree(no1)

    chaves = [no2,None,None,no3]
    teste_arvore.inserir(no1,chaves)

    chaves = [no4,no1,None,no5]
    teste_arvore.inserir(no2,chaves)

    chaves = [no6,no1,None,no7]
    teste_arvore.inserir(no3,chaves)

    aux = teste_arvore.buscarPuzzleReal(teste_arvore.retornaRoot(),no5)
    print('aux:',aux)

    print(teste_arvore.converterFolhas(teste_arvore.irFolha(teste_arvore.retornaRoot())))

    print("FINAL")