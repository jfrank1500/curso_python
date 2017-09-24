a = float(raw_input('Angulo A? '))
b = float(raw_input('Angulo B? '))
c = float(raw_input('Angulo C? '))
if (a == 90.0) or (b == 90.0) or (c == 90.0):
    print 'Triangulo retangulo'
elif (a > 90.0) or (b > 90.0) or (c > 90.0):
    print 'Triangulo obtusangulo'
elif (a < 90.0) and (b < 90.0) and (c < 90.0):
    print 'Triangulo acutangulo'
