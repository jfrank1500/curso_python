# Entrada
a = int(raw_input('Lado A? '))
b = int(raw_input('Lado B? '))
c = int(raw_input('Lado C? '))
# Processamento
if a > b + c:
  print 'Não é um triangulo'
elif b > a + c:
  print 'Não é um triangulo'
elif c < a + b:
  print 'Não é um triangulo'
else:
  print 'É um triangulo'