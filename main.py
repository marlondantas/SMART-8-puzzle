from eightpuzzle import *
from metodoBusca import *


# inicio = eightPuzzle('RANDOM')

inicio = eightPuzzle([['1','3','5'],['X','8','2'],['4','7','6']])

fim    = eightPuzzle([['1','2','3'],
                      ['4','5','6'], 
                      ['7','8','X']])


sol = metodoBusca()

amplitude = sol.amplitude(inicio,fim)

##Coisas para otimizacao, Primeiro, Não guardar puzzle mas sim strings
##Eliminar puzzle com todos os filhos possiveis que não estão dentro do bagulho... talvez possivel problema com os pais....
##recursividade e fors da vida...
##guarda dados para analise... formato compativel com BI

sol.impResultado(amplitude)


