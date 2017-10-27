'''------------------------------------------------------------------------------------------
| Tarefa 9 - Implementar um algoritmo genético para resolver um problema de minimização     |
| 																							|
| Renan Mateus Bernardo Nascimento															|
| Vinícius Magalhães D'Assunção																|
------------------------------------------------------------------------------------------'''

import numpy as np

class Cromossomo:

	def __init__(self, variaveis):
		self.alelos = np.zeros(variaveis)
		self.aptidao = 0.0