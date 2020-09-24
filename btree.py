class node(object):
    def __init__(self, puzzle=None, keys = [None,None,None,None]):

        self.puzzle    = puzzle
        self.id_puzzle = str(puzzle)

        #Opcoes       #C   B    E    D  
        self.keys = keys


# raizCima2 = node('123456723')
# raizCima = node('123456798',[raizCima2,None,None,None])
# raizbaixo = node('123456798')
# raizesquerda = node('123456798')
# raizdireita = node('123456798')

# raizPadrao = node('123456789',[raizCima,raizbaixo,raizesquerda,raizdireita])


class tree(object):
    __root = None
    inseridos = []
    
    def __init__ (self,puzzle):
        if(puzzle != None):
            self.insereRoot(puzzle)
        

    def insereRoot(self, puzzle):
        self.__root = puzzle
        self.inseridos.append(puzzle.id_puzzle)

    def buscarPuzzle(self,id_puzzle):
        if(self.__root != None):
            aux = self.__root
            
            # Cima
            i = 0
            while i < 4: 
                while (aux.keys[i] != None):
                    if(aux.keys[i].id_puzzle == id_puzzle):
                        return str(i)+" "+ aux.keys[i].id_puzzle
                    else:
                        aux.keys[i] = aux.keys[i].keys[i]
                i = i + 1
            return "Valor não encontrado"

            # while aux != None:
            #     if(aux.id_puzzle == id_puzzle):
            #         return aux
            #     else:
            #         aux
        else:
            return ('Btree Empty')

    def insereKeys(self, id_puzzle,keys):
        if(self.__root != None):
            aux = self.__root
            
            # Cima
            i = 0
            while i < 4: 
                sair = 0
                while (aux.keys[i] != None):
                    if(aux.keys[i].id_puzzle == id_puzzle):
                        sair = 1
                        break
                    else:
                        aux.keys[i] = aux.keys[i].keys[i]
                if(sair != 0):
                    break

                i = i + 1
            if(aux == None):
                print("Puzzle não encontrado")
                return 1
            else:
                aux.keys = keys

                for x in range(4):
                    if(aux.keys[x] != None):
                        self.inseridos.append(aux.keys[x].id_puzzle)

                return aux
        else:
            return ('Btree Empty')

# nova_tree = tree(raizPadrao)
# print(nova_tree.buscarPuzzle('123456723'))

# raizbaixo2 = node('951753852')

# nova_tree.insereKeys('123456723',[None,raizbaixo2,None,None])

# print(nova_tree.buscarPuzzle('951753852'))

# print("Fim da arvore")