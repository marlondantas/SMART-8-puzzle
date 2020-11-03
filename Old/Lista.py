class node(object):
    def __init__(self, pai=None, puzzle=None, leaf=None, anterior=None, proximo=None):
        self.pai       = pai

        self.puzzle    = puzzle
        self.id_puzzle = str(puzzle)

                      #C   B    E    D  
        self.keys = [None,None,None,None]

        self.leaf  = leaf

        self.anterior  = anterior
        self.proximo   = proximo

class lista(object):
    __head = None;
    __tail = None;
    
    __root = None;
    
    def insereRoot(self, puzzle):
        self.__root = puzzle

    def 
    #Novo item no inico da lista
    def inserePrimeiro(self, puzzle, leaf=True, pai=None):

        novo_no = node(pai, puzzle, leaf, None, None)

        if self.__head == None:
            self.__tail = novo_no
        else:
            novo_no.proximo = self.__head
            self.__head.anterior = self.__tail
        
        self.__head  = novo_no

    #Noto item no final da lista
    def insereUltimo(self, valor, leaf=True, pai=None):
        novo_no = node(pai,valor,leaf)

        if self.__head == None:
            self.__head = novo_no
        else:
            self.__tail.proximo = novo_no
            novo_no.anterior = self.__tail
        
        self.__tail = novo_no

    #Remover item do inico da lista
    def deletaPrimeiro(self):
        if self.__head == None:
            return None
        else:
            node = self.__head

            self.__head = self.__head.proximo

            if self.__head != None:
                self.__head.anterior = None
            else:
                self.__tail = None

            return node
            
    #Remover item do fim da lista
    def deletaUltimo(self):
        if self.__tail == None:
            return None
        else:
            node = self.__tail

            self.__tail = self.__tail.anterior
            if self.__tail != None:
                self.__tail.proximo = None
            else:
                self.__head = None
            
            return node

    #Verifica se a lista está vazia
    def vazia(self):
        if self.__head == None:
            return True
        else:
            return False
        
    #Mostrar o conteudo da lista
    def mostrarLista(self):

        saida = []
        aux = self.__head
        while aux != None:
            saida.append(aux.puzzle.getConteudo())
            aux = aux.proximo

        return saida
    
    #Mostar o caminho (?)
    def exibeCaminho(self):
        
        aux = self.__head
        saida = []
        
        while aux != None:
            saida.append(aux.puzzle.getConteudo())
            aux = aux.proximo
        
        return saida

    #Busca o caminho ate um valor
    def caminhoValor(self,valor):
        atual = self.__head

        while (atual.puzzle != valor):
            atual = atual.proximo
        
        caminho = []
        atual = atual.pai

        while autal.pai is not None:
            caminho.append(atual.puzzle)
            atual = atual.pai
        
        caminho.append(atual.puzzle)
        return caminho

    #Retornar a cabeça da lista
    def primero(self):
        return self.__head
    
    #Retornar a cauda da lista 
    def ultimo(self):
        return self.__tail


superLista = lista()


teste = [['x','4','2'],
         ['3','1','5'],
         ['6','7','8']]

from eightpuzzle import *

puzzleInicio = eightPuzzle(teste)       

superLista.inserePrimeiro(puzzleInicio)
superLista.insereUltimo(puzzleInicio)
superLista.insereUltimo(puzzleInicio)
superLista.insereUltimo(puzzleInicio)
superLista.insereUltimo(puzzleInicio)
superLista.insereUltimo(puzzleInicio)

print(superLista.exibeCaminho())

# uma_node = node(puzzle=puzzleInicio)