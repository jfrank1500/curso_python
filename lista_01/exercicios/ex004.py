# Entrada
anos  = int(raw_input('Anos? '))
meses = int(raw_input('Meses? '))
dias  = int(raw_input('Dias? '))
# Processamento
vivo=(anos*365) + (meses*30) + dias
# Saida
print 'Dias vivo = ', vivo
