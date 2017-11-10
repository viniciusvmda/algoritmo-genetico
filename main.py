#encoding: utf-8
import sys
from ag import Ag

num_args = len(sys.argv)
if num_args < 7:
    sys.exit("Faltam argumentos: python3 main.py tam_populacao, inicio, fim, tax_cruzamento, tax_mutacao, max_geracoes")

tam_populacao, inicio, fim, tax_cruzamento, tax_mutacao, max_geracoes = (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), int(sys.argv[6]))

ag = Ag(tam_populacao, inicio, fim, tax_cruzamento, tax_mutacao, max_geracoes)
ag.executar()
