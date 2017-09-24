# Entrada
ano_atual = int(raw_input('Atual? '))
ano_nasc  = int(raw_input('Nascimento? '))
# Processamento
idade = ano_atual - ano_nasc
if idade >= 16:
    print 'Pode votar'
else:
    print 'Nao pode'
