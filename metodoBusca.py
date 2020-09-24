from btree import *

class metodoBusca(object):
    def amplitude(self,inicio,fim):

        fifoLista = lista()
        caminhoLista = lista()

        fifoLista.insereUltimo(inicio,0,None)
        caminhoLista.insereUltimo(inicio,0,None)

        linha = [] 
        linha.append(inicio)
        linha.append(0)

        visitados = []
        visitados.append(linha)