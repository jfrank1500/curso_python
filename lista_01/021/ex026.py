# Entrada
inicio = int(raw_input('Inicio? '))
fim = int(raw_input('Fim? '))
if fim > inicio:
    print 'Duracao', fim-inicio
else:
    print 'Duracao', (fim+24)-inicio
