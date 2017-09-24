#Entrada
fixo   = float(raw_input('Salario fixo? '))
vendas = float(raw_input('Vendas? '))
#Processamento
if vendas <= 1500.0:
    # 3% sobre as vendas
    comissao = vendas * 0.03
    acrescimo = 0.0
else:
    # 3% sobre as vendas + 5% sobre o excedente
    comissao  = 0.03 * 1500.0
    acrescimo = 0.05 * (vendas - 1500.0)
#Saida
print 'Comissao', comissao
print 'Acrescimo', acrescimo
print 'Salario total', (fixo + comissao + acrescimo)
