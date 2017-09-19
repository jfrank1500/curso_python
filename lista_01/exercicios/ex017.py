def ler(msg):
    return float(raw_input(msg))
#Entrada
km_inicial = ler('Km inicial(km)?')
km_final   = ler('Km final(km)?')
comb_gasto = ler('Combustivel gasto(l)?')
receita    = ler('Receita(R$)?')
#Processamento
preco = 3.9
dist = km_final - km_inicial
consumo = dist / comb_gasto
gasto = preco * comb_gasto
lucro_liq = receita - gasto
#Saida
print 'Media de consumo (km/l)', consumo
print 'Lucro liquido (R$)', lucro_liq
