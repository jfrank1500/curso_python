# Entrada
morangos = float(raw_input('Morangos(Kg)? '))
macas = float(raw_input('Macas (Kg)? '))
# Processamento
# Calculo do preco das frutas por quantidade
if morangos <= 5.0:
  morangos_preco = 2.5
else:
  morangos_preco = 2.2
if macas <= 5.0:
  macas_preco = 1.8
else:
  macas_preco = 1.5
# Calculo do total para cada fruta
macas_total = macas * macas_preco
morangos_total = morangos * morangos_preco
# Calculo do total sem o desconto
total = macas_total + morangos_total
# Calcula o desconto, se houver
if (morangos + macas > 8.0) or (total > 25.0):
  desconto = total * 0.10
else:
  desconto = 0
# Saída
print 'Total=', total - desconto
