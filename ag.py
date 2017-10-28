#encoding: utf-8
from ag import Ag

tam_populacao, inicio, fim, tax_cruzamento, tax_mutacao, max_geracoes = (10, -600, 600, 0.05, 0.3, 10)
ag = Ag(tam_populacao, inicio, fim, tax_cruzamento, tax_mutacao, max_geracoes)

ag.executar()
ag.imprimirPopulacao()
ag.selecao()