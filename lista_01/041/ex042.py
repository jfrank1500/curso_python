codigo = raw_input('Codigo de origem? ')
if codigo == '1':
  regiao = 'Sul'
elif codigo == '5' or codigo == '6':
  regiao = 'Nordeste'
elif codigo == '2':
  regiao = 'Norte'
elif codigo == '7' or codigo == '8' or codigo == '9':
  regiao = 'Sudeste'
elif codigo == '10':
  regiao = 'Noroeste'
else:
  regiao = 'Importado'
print 'O produto tem origem: ', regiao
