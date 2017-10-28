#encoding: utf-8
'''------------------------------------------------------------------------------------------
| Tarefa 9 - Implementar um algoritmo genético para resolver um problema de minimização     |
| 																							|
| Renan Mateus Bernardo Nascimento															|
| Vinícius Magalhães D'Assunção																|
------------------------------------------------------------------------------------------'''

from ag import Ag

tam_populacao, inicio, fim, tax_cruzamento, tax_mutacao, max_geracoes = (3, -600, 600, 0.05, 0.3, 10)
ag = Ag(tam_populacao, inicio, fim, tax_cruzamento, tax_mutacao, max_geracoes)

ag.executar()
a = ag.selecao()
