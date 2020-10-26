from eightpuzzle import *
# from metodoBusca import *
from metodoBuscaLIST import *
from view import montarView

# # inicio = eightPuzzle('RANDOM')

inicio = eightPuzzle([['X','2','3'],
                      ['1','5','6'], 
                      ['4','7','8']])

# inicio = eightPuzzle([['2','5','8'],['X','1','3'],['4','7','6']])

fim    = eightPuzzle([['1','2','3'],
                      ['4','5','6'], 
                      ['7','8','X']])


sol = metodoBusca()
htmlview = montarView()
print("Amplitude")
dic_amplitude = sol.amplitude(inicio,fim)      
htmlview.atualizarResultado(dic_amplitude)
htmlview.salvarArquivo()

print('-'*50)

print("Profundidade")
dic_profu = sol.profundidade(inicio, fim)
htmlview.atualizarResultado(dic_profu,1)
htmlview.salvarArquivo()

print('-'*50)
print("Profundidade Limitada")
dic_profu_limita = sol.profundidade_limitada(inicio, fim,1000)
htmlview.atualizarResultado(dic_profu_limita)
htmlview.salvarArquivo()

print('-'*50)
print("bidirecional")
dic_bidirecional = sol.bidirecional(inicio, fim)
htmlview.atualizarResultado(dic_bidirecional)
htmlview.salvarArquivo()

print('-'*50)
print("aprofundamento_iterativo")
dic_aprofudamento = sol.aprofundamento_iterativo(inicio, fim,1000)
htmlview.atualizarResultado(dic_aprofudamento)
htmlview.salvarArquivo()

print('-'*50)


print("FIM")

htmlview.showResults()