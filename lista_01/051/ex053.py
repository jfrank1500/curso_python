a = float(raw_input('Lado A? '))
b = float(raw_input('Lado B? '))
c = float(raw_input('Lado C? '))
if (a == b) and (a == c):
    print 'Equilatero'
elif (a == b) or (a == c) or (b == c):
    print 'Isosceles'
else:
    print 'Escaleno'
