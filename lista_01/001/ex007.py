# Entrada
sal_hora=float(raw_input('Salario/Hora? '))
num_horas=float(raw_input('Num horas? '))
# Processamento
salario_bruto = sal_hora * num_horas
imposto = salario_bruto * 0.075
salario = salario_bruto - imposto
print 'Salario bruto', salario_bruto
print 'Salario liquido', salario
