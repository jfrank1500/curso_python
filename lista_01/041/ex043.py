nota1 = float(raw_input('Nota 1? '))
nota2 = float(raw_input('Nota 2? '))
optativa = float(raw_input('Optativa? '))
if optativa != -1:
  if nota1 > nota2:
    nota2 = optativa
  else:
    nota1 = optativa
media = (nota1 + nota2) / 2.0
print 'Media', media
if media >= 6.0:
  print 'Aprovado'
elif media >= 3.0:
  print 'Fazer exame'
else:
  print 'Reprovado'
