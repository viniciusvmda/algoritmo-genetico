#encoding: utf-8
import matplotlib.pyplot as plt
from cromossomo import Cromossomo
import numpy as np
import random


class Ag:

    def __init__(self, tam_populacao, inicio, fim, tax_cruzamento, tax_mutacao, max_geracoes):
        self.tam_populacao = tam_populacao
        # valor inicial para alelos do cromossomo
        self.inicio = inicio
        # Valor final para alelos do cromossomo
        self.fim = fim        
        self.tax_cruzamento = tax_cruzamento
        self.tax_mutacao = tax_mutacao
        self.max_geracoes = max_geracoes
        # offset da função de aptidão
        self.OFFSET = 1500
        self.MAX = 959.6407 + self.OFFSET
        self.QTD_ALELOS = 2
        self.ELITE = 5
        self.populacao = []

    '''
    ' Inicializa a lista de população
    '''
    def popular(self):
        self.populacao = []
        for c in range(0, self.tam_populacao):
            cromo = Cromossomo(self.QTD_ALELOS)
            for a in range(0, len(cromo.alelos)):
                cromo.alelos[a] = random.randrange(self.inicio, self.fim + 1)
            cromo.aptidao = self.calcAptidao(cromo.alelos[0], cromo.alelos[1])
            self.populacao.append(cromo)

    '''
    ' Calcula a função de aptidão de toda a população
    '''
    def calcAptidao(self, x1, x2):
        return self.OFFSET + (x2 + 47) * np.sin(np.sqrt(abs(x2 + x1/2 +47))) + x1 * np.sin(np.sqrt(abs(x1 - (x2 + 47))))
        
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
            # A roleta possui a tupla inicio_intervalo e fim_intervalo como índice do dicionário
            # O valor corresponde ao índice do vetor de população
            roleta[(total, total + c.aptidao)] = i
            total += c.aptidao
        
        # Sorteia tam_populacao/2 números para selecionar na roleta
        for i in range(0, self.tam_populacao):
            # Sorteia o número entre 0(fechado) e a aptidão total(aberto)
            num = random.uniform(0, total)
            for intervalo, c in roleta.items():
                if num >= intervalo[0] and num < intervalo[1]:
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
            # Sorteia um número de 0 a 1 com duas casas decimais
            num = random.randrange(0, 100) / 100
            if num <= self.tax_cruzamento:
                # Porcentagem do cromossomo dos pais que será utilizada no cruzamento
                alfa_cruzamento = random.randrange(0, 100) / 100
                # Se for menor que a taxa de cruzamento, faz o c/home/aluno/Downloadsruzamento aritmético
                qtd_alelos = len(pai.alelos)
                # Cria os cromossomos
                f1 = Cromossomo(qtd_alelos)
                f2 = Cromossomo(qtd_alelos)
                f1.alelos = alfa_cruzamento * pai.alelos + (1 - alfa_cruzamento) * pai2.alelos
                f2.alelos = (1 - alfa_cruzamento) * pai.alelos + alfa_cruzamento * pai2.alelos
                f1.aptidao = self.calcAptidao(f1.alelos[0], f1.alelos[1])
                f2.aptidao = self.calcAptidao(f2.alelos[0], f2.alelos[1])
                # Adiciona a lista de filhos
                filhos.append(f1)
                filhos.append(f2)
            else:
                # Senão apenas propaga os pais
                filhos.append(pai)
                filhos.append(pai2)
        return filhos
    
    '''
    ' Faz a mutação utilizando o método CREEP
    '''
    def mutar(self, filhos):
        n_casas = 1000 # Número de casas decimais para avaliar a mutação
        for cromo in filhos:
            for i in range(0, len(cromo.alelos)):
                # Sorteia um número de 0 a 1 com 3 casas decimais
                num = random.randrange(0, n_casas) / n_casas
                if num <= self.tax_mutacao:
                    delta = random.uniform(-2, 2)
                    cromo.alelos[i] += delta
    
    '''
    ' Substitui o pior filho pelo melhor pai
    '''
    def elitizar(self, filhos):
        # Ordena filhos por ordem decrescente de aptidão
        filhos = sorted(filhos, reverse=True, key = lambda Cromossomo: Cromossomo.aptidao)
        # Ordena pais por ordem decrescente de aptidão
        self.populacao = sorted(self.populacao,reverse=True, key = lambda Cromossomo: Cromossomo.aptidao)
        # Substitui os pelos filhos mantendo os ELITE melhores pais e tirando os ELITE piores filhos
        self.populacao = np.append(filhos[:-self.ELITE], self.populacao[:self.ELITE])
    
    
    '''
    ' Retorna mínimo, média e máximo
    '''
    def retornaMedidas(self):
        total_aptidao = 0
        minimo = self.populacao[0].aptidao
        maximo = self.populacao[0].aptidao
        for cromo in self.populacao:
            total_aptidao += cromo.aptidao
            if cromo.aptidao < minimo:
                minimo = cromo.aptidao
            elif cromo.aptidao > maximo:
                maximo = cromo.aptidao
        return minimo, total_aptidao / self.tam_populacao, maximo
    
    '''
    ' Gera o gráfico Erro x Iteração
    ''' 
    def gerarGrafico(self, tempo, minimo, media, maximo):
        plt.plot(tempo, minimo, label='Mínimo')
        plt.plot(tempo, media, label='Média')
        plt.plot(tempo, maximo, label='Máximo')
        plt.ylabel('Aptidão')
        plt.xlabel('Iteração')
        plt.title('Gráfico Aptidão x Iteração')
        plt.legend()
        plt.show()
       
    
    def melhoresCromossomos(self):
        n_melhores = 3
        melhores = sorted(self.populacao, reverse=True, key = lambda Cromossomo: Cromossomo.aptidao)
        print('Melhores cromossomos:')
        for cromo in melhores[:n_melhores]:
            print(str(cromo.alelos) + '\t=\t' + str(cromo.aptidao))
        
    
    '''
    ' Executa max_geracoes vezes o algoritmo genético
    '''
    def executar(self, elitismo = False):
        self.popular()
        # Inicaliza os vetores de tempo e erro com o estado inicial
        mini, med, maxi = self.retornaMedidas()
        tempo = [0]
        minimo = [mini]
        media = [med]
        maximo = [maxi]
        t = 1
        # Executa o algoritmo genético até o erro ser zero ou atinger o máximo de gerações
        while t <= self.max_geracoes:
            selecao = self.selecionar()
            filhos = self.cruzar(selecao)
            self.mutar(filhos)
            if elitismo:
                self.elitizar(filhos)
            else:
                self.populacao = filhos
            mini, med, maxi = self.retornaMedidas()
            tempo.append(t)
            minimo.append(mini)
            media.append(med)
            maximo.append(maxi)
            t += 1
        # Gera o gráfico de saída
        self.gerarGrafico(tempo, minimo, media, maximo)
        self.melhoresCromossomos()
        

    def imprimirPopulacao(self):
        for c in self.populacao:
            print(str(c.alelos[0]) + '\t' + str(c.alelos[1]) + '\t' + str(c.aptidao))