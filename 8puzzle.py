class eightPuzzle(object):
    
    conteudo = []

    eixoXeY = 0
    numeroMovimentos,ultimoMovimento = 0,''
    #numero de casa = 

    #Movimentacao
    def __moverValor(self,novo,antigo,movimento = ''):
        espacoVazio = novo
        localizaValor= antigo

        lxtmp_puzzle = self.getConteudo() + []

        lxtmp_puzzle[espacoVazio[0]][espacoVazio[1]] = lxtmp_puzzle[localizaValor[0]] [localizaValor[1]]
        lxtmp_puzzle[localizaValor[0]][localizaValor[1]] = 'X'

        self.setConteudo(lxtmp_puzzle)
        
        self.numeroMovimentos = self.numeroMovimentos + 1
        self.ultimoMovimento = movimento

        return True

    def moverCima(self):
        if(self.liberadaCima() == True):
            espacoVazio = self.__localizarEspaco()
            return self.__moverValor(espacoVazio,[espacoVazio[0]+1, espacoVazio[1]],'Cima')
        else:
            print("Não pode mover para cima")
            return False
    def moverBaixo(self):
        if(self.liberadaBaixo() == True):
            espacoVazio = self.__localizarEspaco()
            return self.__moverValor(espacoVazio,[espacoVazio[0]-1, espacoVazio[1]],'Baixo')
        else:
            print("Não pode mover para Baxio")
            return False
    def moverEsquerda(self):
        if(self.liberadaEsquerda() == True):
            espacoVazio = self.__localizarEspaco()
            return self.__moverValor(espacoVazio,[espacoVazio[0], espacoVazio[1]+1],'Esquerda')
        else:
            print("Não pode mover para Esquerda")
            return False
    def moverDireita(self):
        if(self.liberadaDireita() == True):
            espacoVazio = self.__localizarEspaco()
            return self.__moverValor(espacoVazio,[espacoVazio[0], espacoVazio[1]-1],'Direita')
        else:
            print("Não pode mover para Direita")
            return False

    #Localizar espaco vazio
    def __localizarEspaco(self):
        espacoVazio = []

        linha = 0
        coluna = 0
        while espacoVazio == []:

            if(self.conteudo[linha][coluna].upper() == 'X'):
                espacoVazio = [linha,coluna]
            else:
                coluna = coluna + 1
            
            if coluna == self.eixoXeY:
                linha = linha + 1
                coluna = 0
        
        return espacoVazio
    
    #Checar se é possivel (true) pode / (false) não pode
    def liberadaCima(self):
        espacoVazio = self.__localizarEspaco()
        
        if espacoVazio[0] != self.eixoXeY - 1:
            return True
        else:
            return False
    def liberadaBaixo(self):
        espacoVazio = self.__localizarEspaco()
     
        if espacoVazio[0] != 0:
            return True
        else:
            return False       
    def liberadaEsquerda(self):
        espacoVazio = self.__localizarEspaco()

        if espacoVazio[1] != self.eixoXeY - 1:
            return True
        else:
            return False 
    def liberadaDireita(self):
        espacoVazio = self.__localizarEspaco()

        if espacoVazio[1] != 0:
            return True
        else:
            return False 

    def liberadaOpcoes(self):
        return [self.liberadaCima(),self.liberadaBaixo(),self.liberadaDireita(),self.liberadaEsquerda()]

    #Conteudo
    def setConteudo(self,puzzle):
        self.conteudo = puzzle
        self.eixoXeY = len(puzzle)
    
    def getConteudo(self):
        return self.conteudo
    
    def printConteudo(self):
        print('|N:',self.numeroMovimentos,'|M:',self.ultimoMovimento)
        print('----------------')
        for x in self.conteudo:
            print('|',end='')
            for y in x:
                print(' ',y,'|',end='')
            print()
        print('----------------')

    def __init__(self,puzzle):
        self.setConteudo(puzzle)
    def __str__(self):
        saida = ''
        
        for x in self.getConteudo():
            for y in x:
                saida = saida + y
        
        return saida

# teste = [['x','4','2'],
#          ['3','1','5'],
#          ['6','7','8']]

# puzzleInicio = eightPuzzle(teste)

# print("Movendo")
# puzzleInicio.printConteudo()

# puzzleInicio.moverCima()#1
# puzzleInicio.printConteudo()

# puzzleInicio.moverEsquerda()#2
# puzzleInicio.printConteudo()

# puzzleInicio.moverEsquerda()#3
# puzzleInicio.printConteudo()

# puzzleInicio.moverBaixo()#4
# puzzleInicio.printConteudo()

# puzzleInicio.moverDireita()#5
# puzzleInicio.printConteudo()

# print(puzzleInicio)