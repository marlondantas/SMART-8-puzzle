from eightpuzzle import *
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

# inicio = eightPuzzle([['2','8','3'],
#                         ['1','6','4'], 
#                         ['7','X','5']])

# # inicio = eightPuzzle([['1','2','3'],['4','8','5'],['7','X','6']])

# fim    = eightPuzzle([['1','2','3'],
#                         ['8','X','4'], 
#                         ['7','6','5']])

sol = metodoBusca()
htmlview = montarView(inicio,fim)

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
print("custouniforme")
dic_aprofudamento = sol.custoUniforme(inicio, fim)
htmlview.atualizarResultado(dic_aprofudamento)
htmlview.salvarArquivo()

print('-'*50)
print("Greedy")
dic_aprofudamento = sol.greedy(inicio, fim)
htmlview.atualizarResultado(dic_aprofudamento)
htmlview.salvarArquivo()

print('-'*50)
print("aEstrela")
dic_aprofudamento = sol.aEstrela(inicio, fim)
htmlview.atualizarResultado(dic_aprofudamento)
htmlview.salvarArquivo()

print('-'*50)
print("FIM")

htmlview.showResults()