# Entrada
num_carros=float(raw_input('Num carros? '))
total_vendas=float(raw_input('Total vendas'))
salario_fixo=float(raw_input('SF? '))
comissao=float(raw_input('Comissao? '))
# Processamento
salario_final=salario_fixo + \
              comissao * num_carros + \
              0.05 * total_vendas              
# Saida
print 'Salario final', salario_final
