#encoding: utf-8

from ag import Ag

tam_populacao, inicio, fim, alfa, tax_cruzamento, tax_mutacao, max_geracoes = (100, -600, 600, 0.6, 0.6, 0.005, 1000)
elitismo = True

ag = Ag(tam_populacao, inicio, fim, alfa, tax_cruzamento, tax_mutacao, max_geracoes)
ag.executar(elitismo)
