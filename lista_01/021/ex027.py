# Entrada
horas_trabalhadas = float(raw_input('Horas trabalhadas no mes? '))
salario_hora = float(raw_input('Salario por hora? '))
# Processamento
jornada_semanal = 40.0                  # 40 horas
jornada_mensal  = jornada_semanal * 4.0 # 4 semanas
if horas_trabalhadas <= jornada_mensal:
    # Nao houve horas extras
    salario = horas_trabalhadas * salario_hora
else:
    # Houve horas extras
    sobrejornada = horas_trabalhadas - jornada_mensal
    salario = (jornada_mensal * salario_hora) + (sobrejornada * 1.5 * salario_hora)
print 'Salario', salario
