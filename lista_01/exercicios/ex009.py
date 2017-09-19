# Entrada
salario = float(raw_input('Salario? '))
reajuste = float(raw_input('Reajuste? '))
# Processamento
reajuste = reajuste / 100.0
novo_salario=salario+salario*reajuste
# Saida
print 'Novo salario', novo_salario
