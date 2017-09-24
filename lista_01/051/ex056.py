n1 = float(raw_input('N1? '))
n2 = float(raw_input('N2? '))
n3 = float(raw_input('N3? '))
exercicios = float(raw_input('Media dos exercicios? '))
aproveitamento = (n1 + 2.0 * n2 + 3.0 * n3 + exercicios) / 7.0
print 'Aproveitamento=', aproveitamento
if aproveitamento >= 9.0:
    print 'Conceito A'
elif aproveitamento >= 7.5:
    print 'Conceito B'
elif aproveitamento >= 6.0:
    print 'Conceito C'
else:
    print 'Conceito D'
