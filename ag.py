#encoding: utf-8
'''------------------------------------------------------------------------------------------
| Tarefa 9 - Implementar um algoritmo genético para resolver um problema de minimização     |
| 																							|
| Renan Mateus Bernardo Nascimento															|
| Vinícius Magalhães D'Assunção																|
------------------------------------------------------------------------------------------'''

import numpy as np
from cromossomo import Cromossomo

class Ag:

	def __init__(self, tamanho, inicio, fim, tax_cruzamento, tax_mutacao, max_geracoes):
		self.tamanho = tamanho					# tamanho da população
		self.inicio = inicio					# valor inicial para alelos do cromossomo
		self.fim = fim							# valor final para alelos do cromossomo
		self.tax_cruzamento = tax_cruzamento	# taxa de cruzamento
		self.tax_mutacao = tax_mutacao			# taxa de mutação
		self.max_geracoes = max_geracoes		# número máximo de gerações
		self.populacao = []

		self.popular()


	'''
	' Inicializa a lista de população
	'''
	def popular(self):
		pass

	'''
	' Calcula a função de aptidão de toda a população
	'''
	def calcAptidao(self):
		'''for cromossomo in self.populacao:
			cromossomo.alelo = '''
		pass

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
		pass