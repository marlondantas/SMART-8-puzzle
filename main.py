from eightpuzzle import *
from metodoBusca import *


inicio = eightPuzzle('RANDOM')

fim    = eightPuzzle([['1','2','3'],
                      ['4','5','6'], 
                      ['7','8','X']])


sol = metodoBusca()

amplitude = sol.amplitude(inicio,fim,debug=1)

sol.impResultado(amplitude)


