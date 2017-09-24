# Entrada
a = int(raw_input('A? '))
b = int(raw_input('B? '))
c = int(raw_input('C? '))
# Processamento
ab = a + b
ac = a + c
bc = b + c
if ab > ac:
  if ab > bc:
    print ab
  else:
    print bc
else:
  if ac > bc:
    print ac
  else:
    print bc 