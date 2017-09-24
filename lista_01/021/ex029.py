#Entrada
conta = raw_input('Conta? ')
saldo = float(raw_input('Saldo? '))
debito = float(raw_input('Debito? '))
credito = float(raw_input('Credito? '))
#Processamento
saldo_atual = saldo - debito + credito
if saldo_atual >= 0:
    print 'Saldo positivo'
else:
    print 'Saldo negativo'
#Saida
print 'Saldo atual R$', saldo_atual
