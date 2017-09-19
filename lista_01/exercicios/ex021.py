#Entrada
macas = int(raw_input('Macas? '))
# Processamento
if macas < 12:
    total = 1.3 * macas
else:
    total = 1.0 * macas
# Saida
print 'Total', total
