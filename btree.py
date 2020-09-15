class node(object):
    def __init__(self, pai=None, puzzle=None, visitado=None, anterior=None, proximo=None):
        self.pai       = pai

        self.puzzle    = puzzle
        self.visitado  = visitado

        self.anterior  = anterior
        self.proximo   = proximo

class lista(object):
    head = node;
    tail = node;

    #Novo item no inico da lista
    def inserePrimeiro(self, v1, v2, pai):
        novo_no = node(pai,v1,v2,None,None)

        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = self.tail
        
        self.tail = novo_no

    #Noto item no final da lista
    def insereUltimo(self, valor, visitado, pai):
        novo_no = node(pai,valor,visitado)

        if self.head == None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior = self.tail
        
        self.tail = novo_no

    #Remover item do inico da lista
    def deletaPrimeiro(self):
        if self.head = None:
            return None
        else:
            node = self.head

            self.head = self.head.proximo

            if self.head != None:
                self.head.anterior = None
            else:
                self.tail = None

            return node
            
    #Remover item do fim da lista
    def deletaUltimo(self):
        if self.tail = None:
            return None
        else:
            node = self.tail

            self.tail = self.tail.anterior
            if self.tail != None:
                self.tail.proximo = None
            else:
                self.head = None
            
            return node

    #Verifica se a lista está vazia
    def vazia(self):
        if self.head = None:
            return True
        else:
            return False
        
    #Mostrar o conteudo da lista
    def mostrarLista(self):

        saida = []
        aux = self.head
        while aux != None:
            saida.append(aux.puzzle)
            aux = aux.proximo

        return saida
    
    #Mostar o caminho (?)
    def exibeCaminho(self):
        
        aux = self.head
        saida = []
        
        while aux != None:
            saida.append(aux.puzzle)
            aux = aux.proximo
        
        return saida

    #Busca o caminho ate um valor
    def caminhoValor(self,valor):
        atual = self.head

        while atual.puzzle != valor
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
        return self.head
    
    #Retornar a cauda da lista 
    def ultimo(self):
        return self.tail
















lista_teste = lista()
lista_teste.inserePrimeiro(['1','2','3'],0,None)