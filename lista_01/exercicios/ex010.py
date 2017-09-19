# Entrada
custo_fab=float(raw_input('Custo fab? '))
# Processamento
custo_dist=0.28*custo_fab
impostos  =0.45*custo_fab
custo_final=custo_fab+custo_dist+impostos
# Saida
print 'Custo final', custo_final
