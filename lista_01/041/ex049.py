numero = int(raw_input('Numero de lados? '))
medida = int(raw_input('Medida do lado? '))
if numero == 3:
  print 'Triangulo. Perimetro=', 3 * medida
elif numero == 4:
  print 'Retangulo. Area=', medida * medida
elif numero == 5:
  print 'Pentagono'