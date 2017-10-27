#encoding: utf-8
'''------------------------------------------------------------------------------------------
| Tarefa 9 - Implementar um algoritmo genético para resolver um problema de minimização     |
| 																							|
| Renan Mateus Bernardo Nascimento															|
| Vinícius Magalhães D'Assunção																|
------------------------------------------------------------------------------------------'''

import numpy as np
import random
from cromossomo import Cromossomo


class Ag:

	def __init__(self, tam_populacao, inicio, fim, tax_cruzamento, tax_mutacao, max_geracoes):
		self.tam_populacao = tam_populacao		# tamanho da população
		self.inicio = inicio					# valor inicial para alelos do cromossomo
		self.fim = fim							# valor final para alelos do cromossomo
		self.tax_cruzamento = tax_cruzamento	# taxa de cruzamento
		self.tax_mutacao = tax_mutacao			# taxa de mutação
		self.max_geracoes = max_geracoes		# número máximo de gerações
		self.OFFSET = 1500						# offset da função de aptidão
		self.QTD_ALELOS = 2
		self.populacao = []


	'''
	' Inicializa a lista de população
	'''
	def popular(self):
		for c in range(0, self.tam_populacao):
			cromosssomo = Cromossomo(self.QTD_ALELOS)
			for a in range(0, len(cromosssomo.alelos)):
				cromosssomo.alelos[a] = random.randrange(self.inicio, self.fim + 1)
			self.populacao = np.append(self.populacao, cromosssomo)


	'''
	' Calcula a função de aptidão de toda a população
	'''
	def calcAptidao(self):
		for c in self.populacao:
			x1, x2 = (c.alelos[0], c.alelos[1])
			c.aptidao = self.OFFSET + (x2 + 47) * np.sin(np.sqrt(abs(x2 + x1/2 +47))) + x1 * np.sin(np.sqrt(abs(x1 - (x2 + 47))))


	'''
	' Faz a seleção da população utilizando o método da roleta
	'''
	def selecao(self):
		pass

	'''
	' Faz o cruzamento utilizando o método aritmético
	'''
	def cruzamento(self):
		pass

	'''
	' Faz a mutação utilizando o método CREEP
	'''
	def mutacao(self):
		pass

	'''
	' Executa max_geracoes vezes o algoritmo genético
	'''
	def executar(self):
		self.popular()


	def imprimirPopulacao(self):
		for c in self.populacao:
			print(str(c.alelos[0]) + '\t' + str(c.alelos[1]) + '\t' + str(c.aptidao))