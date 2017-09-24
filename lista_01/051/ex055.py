nome = raw_input('Nome? ')
quantidade = float(raw_input('Quantidade adquirida? '))
preco = float(raw_input('Preco unitario? '))
total = quantidade * preco
if quantidade <= 5.0:
    desconto = total * 0.02 # 2%
elif quantidade <= 10.0: 
    desconto = total * 0.03 # 3%
else
    desconto = total * 0.1 # 10%
total_pagar = total - desconto
print 'Total a pagar', total_pagar
