# Entrada
tipo = raw_input('Tipo do combustivel (A-alcool, G-gasolina)? ')
litros = float(raw_input('Quantos litros? '))
# Processamento
if tipo == 'A':
  if litros < 20.0:
    desconto = 0.03
  else:
    desconto = 0.05
  total = litros * 2.9 * (1-desconto)
if tipo == 'G':
  if litros < 20.0:
    desconto = 0.04
  else:
    desconto = 0.06
  total = litros * 3.3 * (1-desconto)
# Saida
print 'Total', total
