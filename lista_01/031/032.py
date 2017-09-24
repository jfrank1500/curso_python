# Entrada
a = int(raw_input('A? '))
b = int(raw_input('B? '))
c = int(raw_input('C? '))
# Processamento
if a > b:
  if a > c:
    print 'A é maior que B e C', a
  else:
    print 'C é maior que A e B', c
else:
  if b > c:
    print 'B é maior que A e C', b
  else:
    print 'C é maior que A e B', c