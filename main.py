#encoding: utf-8
'''------------------------------------------------------------------------------------------
| Tarefa 9 - Implementar um algoritmo genético para resolver um problema de minimização     |
| 																							|
| Renan Mateus Bernardo Nascimento															|
| Vinícius Magalhães D'Assunção																|
------------------------------------------------------------------------------------------'''

from ag import Ag


tamanho, inicio, fim, tax_cruzamento, tax_mutacao, max_geracoes = (1, 1, 1, 1, 1, 1)
ag = Ag(tamanho, inicio, fim, tax_cruzamento, tax_mutacao, max_geracoes)