#encoding: utf-8
import numpy as np
import random
from cromossomo import Cromossomo

class Ag:

    def __init__(self, tam_populacao, inicio, fim, tax_cruzamento, tax_mutacao, max_geracoes):
        self.tam_populacao = tam_populacao
        # valor inicial para alelos do cromossomo
        self.inicio = inicio
        # valor final para alelos do cromossomo
        self.fim = fim
        self.tax_cruzamento = tax_cruzamento
        self.tax_mutacao = tax_mutacao
        self.max_geracoes = max_geracoes
        # offset da função de aptidão
        self.OFFSET = 1500
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
            self.populacao.append(cromosssomo)
        self.calcAptidao()

    '''
    ' Calcula a função de aptidão de toda a população
    '''
    def calcAptidao(self):
        for c in self.populacao:
            x1, x2 = (c.alelos[0], c.alelos[1])
            c.aptidao = self.OFFSET + (x2 + 47) * np.sin(np.sqrt(abs(x2 + x1/2 +47))) + x1 * np.sin(np.sqrt(abs(x1 - (x2 + 47))))


    '''
    ' Faz a seleção da população utilizando o método da roleta
    ' @return selecao
    '''
    def selecionar(self):
        selecao = []
        roleta = {}
        total = 0
        
        # Adiciona índice do cromossomo à roleta
        for i, c in enumerate(self.populacao):
            roleta[(total, total + c.aptidao)] = i
            total += c.aptidao
        
        # Sorteia tam_populacao/2 números para selecionar na roleta
        for i in range(0, int(self.tam_populacao/2)):
            num = random.uniform(0, total + 1)
            for intervalo, c in roleta.items():
                if num > intervalo[0] and num <= intervalo[1]:
                    selecao.append(c)
                    
        return selecao
    
    
    '''
    ' Faz o cruzamento utilizando o método aritmético
    '''
    def cruzar(self, selecao):
        selecao = self.selecionar()
        filhos = []
        for i in range(0, int(len(selecao)/2)):
            (pai, pai2) = (self.populacao[selecao[2 * i]], self.populacao[selecao[2 * i + 1]])
            # Faz o cruzamento
            f1 = self.tax_cruzamento * pai.alelos + (1 - self.tax_cruzamento) * pai.alelos
            f2 = (1 - self.tax_cruzamento) * pai.alelos + self.tax_cruzamento * pai.alelos
            filhos.append(f1)
            filhos.append(f2)
            
        return filhos
    
    '''
    ' Faz a mutação utilizando o método CREEP
    '''
    def mutar(self):
        pass

    '''
    ' Executa max_geracoes vezes o algoritmo genético
    '''
    def executar(self):
        self.popular()
        #selecao = self.selecionar()
        #cruzamento = self.cruzar(selecao)

    def imprimirPopulacao(self):
        for c in self.populacao:
            print(str(c.alelos[0]) + '\t' + str(c.alelos[1]) + '\t' + str(c.aptidao))