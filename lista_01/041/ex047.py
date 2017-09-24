altura = float(raw_input('Altura? '))
sexo = raw_input('Sexo? 1-Feminino 2-Masculino ')
if sexo == '1':
  peso = (62.1 * altura) - 44.7
else:
  peso = (72.7 * altura)
print 'Peso ideal=', peso
