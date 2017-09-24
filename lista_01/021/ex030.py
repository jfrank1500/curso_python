#Entrada
estoque = raw_input('Quantidade atual em estoque? ')
maxima = float(raw_input('Quant maxima? '))
minima = float(raw_input('Quant minima? '))
#Processamento
media = (maxima + minima)/2.0 
if estoque >= media:
    print 'Nao efetuar compra'
else:
    print 'Efetuar compra'
