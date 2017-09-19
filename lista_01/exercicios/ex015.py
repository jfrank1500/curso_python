# -*- coding: utf-8 -*-
#Entrada
pot =float(raw_input('Potencia? '))
larg=float(raw_input('Largura? '))
comp=float(raw_input('Comprimento? ')) 
#Processamento
potnec=larg * comp * 18.0
lampadas = potnec / pot
#Saida
print 'Lampadas ', lampadas
