# Entrada
aptos   = int(raw_input('Eleitores? '))
brancos = int(raw_input('Brancos? '))
nulos   = int(raw_input('Nulos? '))
validos = int(raw_input('Validos? '))
# Processamento
p_brancos = float(brancos) / aptos
p_nulos   = float(nulos) / aptos
p_validos = float(validos) / aptos
# Saida
print 'Percentual brancos ', p_brancos
print 'Percentual nulos ', p_nulos
print 'Percentual validos ', p_validos
