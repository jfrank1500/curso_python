from datetime import datetime
# Entrada
matricula = raw_input('Matricula do empregado? ')
ano_nascimento = int(raw_input('Ano do nascimento? '))
ano_ingresso = int(raw_input('Ano de ingresso? '))
# Processsamento
agora = datetime.now()
ano_atual = agora.year
idade = ano_atual - ano_nascimento
tempo_trabalhado = ano_atual - ano_ingresso
pode_aposentar = (idade >= 65) or \
   (tempo_trabalhado >= 30) or \
   (idade >= 60 and tempo_trabalhado >= 25)
# Saida
print 'Idade:', idade
print 'Tempo trabalhado:', tempo_trabalhado
if pode_aposentar:
    print 'Pode aposentar'
else:
    print 'Nao pode aposentar'
