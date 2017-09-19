def ler(msg):
    return float(raw_input(msg))
#Entrada
alt  = ler('Altura? ')
comp = ler('Comprimento? ')
larg = ler('Largura? ')
#Processamento
area  = (2.0*larg*alt)+(2.0*comp*alt)
caixas= round(area/1.5)
#Saida
print 'Area', area
print 'Caixas', caixas
