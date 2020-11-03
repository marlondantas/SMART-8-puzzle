class node(object):
    def __init__(self, puzzle=None):
        self.pai = None

        self.puzzle    = puzzle
        self.id_puzzle = str(puzzle)

        self.anterior = None
        self.proximo = None

        self.keys = [None,None,None,None]

        self.heuristica = 0
        self.custo = 0

class Blista(object):
    total_nodes = 0

    __head = None
    __tail = None

    def insertHead(self,node):
        if self.__head == None:
            self.__tail = node
            self.total_nodes = self.total_nodes + 1
        else:
            #verificar se nao existe
            if(self.readNode(node) == None):
                node.proximo = self.__head
                self.__head.anterior = node
                self.total_nodes = self.total_nodes + 1
            else:
                print("Ja existe!")
                return "Ja existe!"
        self.__head = node

    def insertTail(self, node, debug = 0 ):
        if(self.__head == None):
            self.__head = node
            self.total_nodes = self.total_nodes + 1
        else:
            #verificar se nao existe
            if(self.readNode(node) == None):
                self.__tail.proximo = node
                node.anterior = self.__tail
                self.total_nodes = self.total_nodes + 1
            else:
                if(debug == 1):
                    print("Ja existe!")

                return None
        self.__tail = node
    
    def deleteHead(self):
        #pop head
        if self.__head is None:
            return None
        else:
            no = self.__head
            self.__head = self.__head.proximo

            if self.__head is not None:
                self.__head.anterior = None
            else:
                self.__tail = None
            return no

    def deleteTail(self):
        #pop tail
        if self.__tail is None:
            return None
        else:
            no = self.__tail
            self.__tail = self.__tail.anterior

            if self.__tail is not None:
                self.__tail.proximo = None
            else:
                self.__head = None
            
            return no

    def updateNode(self,node):
        #busca o node que corresponde e atualiza ele!
        if(self.__head.id_puzzle == node.id_puzzle):
            node.proximo = self.__head.proximo
            self.__head = node
            return self.__head

        while self.__head.proximo != None:
            if(self.__head.proximo.id_puzzle == node.id_puzzle):
                node.proximo = self.__head.proximo.proximo
                self.__head.proximo = node
                return self.__head
            self.__head = self.__head.proximo
        return None

    def readLeaf(self):
        saida = []

        aux = self.__head
        while aux != None:
            if(aux.keys == [None,None,None,None]):
                saida.append(aux)
            aux = aux.proximo

        return saida

    def readAll(self):
        saida = []

        aux = self.__head
        while aux != None:
            saida.append(aux)
            aux = aux.proximo
        
        return saida
    
    def readNode(self,node):
        saida = None

        aux = self.__head
        while aux != None:
            if(aux.id_puzzle == node.id_puzzle):
                saida = []
                saida.append(aux)
                while aux.pai != None:
                    saida.append(aux.pai)
                    aux = aux.pai
                return saida
            aux = aux.proximo

        return saida

    def readHead(self):
        return self.__head

    def readTail(self):
        return self.__tail


#Testes
if __name__ == "__main__":
    from eightpuzzle import *

    no1 = node(eightPuzzle(puzzle=[['X','2','3'],
                            ['1','5','6'], 
                            ['4','7','8']]))
                        #   raiz

    no2 = node(eightPuzzle(puzzle=[['1','2','3'],
                            ['x','5','6'], 
                            ['4','7','8']]))
    no2.pai = no1
    no3 = node(eightPuzzle([['2','X','3'],
                            ['1','5','6'], 
                            ['4','7','8']]))
    no3.pai = no1

    listona = Blista()
    listona.insertTail(no1)

    no1.keys =[no2,None,None,no3]

    listona.updateNode(no1)
    listona.insertTail(no2)
    listona.insertTail(no3)

    print(listona.readAll())
    print(listona.readLeaf())
    print("caminho ao 3",listona.readNode(no3))
    # no3 = node(eightPuzzle([['2','X','3'],
    #                         ['1','5','6'], 
    #                         ['4','7','8']]))
    #                     # nivel 4

    # no4 = node(eightPuzzle([['1','2','3'],
    #                         ['4','5','6'], 
    #                         ['X','7','8']]))

    # no5 = node(eightPuzzle([['1','2','3'],
    #                         ['5','X','6'], 
    #                         ['4','7','8']]))

    # no6 = node(eightPuzzle([['2','5','3'],
    #                         ['1','X','6'], 
    #                         ['4','7','8']]))

    # no7 = node(eightPuzzle([['2','3','X'],
    #                         ['1','5','6'], 
    #                         ['4','7','8']])) 
    #                     #nivel 3        
                                    
