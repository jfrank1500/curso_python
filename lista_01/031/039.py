# Entrada
h1 = int(raw_input('Idade do homem 1? '))
h2 = int(raw_input('Idade do homem 2? '))
m1 = int(raw_input('Idade da mulher 1? '))
m2 = int(raw_input('Idade da mulher 2? '))
# Processamento
if h1 > h2:
  homem_mais_velho = h1
  homem_mais_novo = h2
else:
  homem_mais_velho = h2
  homem_mais_novo = h1
if m1 > m2:
  mulher_mais_velha = m1
  mulher_mais_nova = m2
else:
  mulher_mais_velha = m2
  mulher_mais_nova = m1
# Saida
print 'Soma=', homem_mais_velho + mulher_mais_nova
print 'Produto=', homem_mais_novo * mulher_mais_velha  
