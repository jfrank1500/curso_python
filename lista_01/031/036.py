# Entrada
a_nome = raw_input('Nome do time A? ')
a_gols = int(raw_input('Gols do time A? '))
b_nome = raw_input('Nome do time B? ')
b_gols = int(raw_input('Gols do time B? '))

# Processamento
if a_gols > b_gols:
  print a_nome, 'venceu'
if a_gols < b_gols:
  print b_nome, 'venceu'
if a_gols == b_gols:
  print 'EMPATE'
