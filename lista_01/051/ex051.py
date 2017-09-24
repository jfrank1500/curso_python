a = int(raw_input('A? '))
b = int(raw_input('B? '))
op = int(raw_input('Operacao (1. Adição, 2. Subtração, 3. Divisão, 4. Multiplicação)? '))
if op == 1:
    resultado = a + b
elif op == 2:
    resultado = a - b
elif op == 3:
    resultado = a * b
elif op == 4:
    resultado = a / b
print 'Resultado=', resultado
